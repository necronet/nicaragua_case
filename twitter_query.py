import sys
import json
import tweepy
import time
from tweepy.error import TweepError
from tweepy.streaming import StreamListener
from datetime import datetime, date, timedelta
from collections import Counter
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from tweepy import Stream
from config import get_twitter_config
from search_terms import get_dates, get_queries
import logging
import random

logging.basicConfig(filename='nicaragua_case.log',level=logging.INFO)

config = get_twitter_config()

if __name__ == '__main__':
    #This handles Twitter authetification and the connection to Twitter Streaming API
    auth = OAuthHandler(config['consumer_key'], config['consumer_secret'])
    auth.set_access_token(config['access_token'], config['access_token_secret'])
    api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

    dates = get_dates(21)
    queries = get_queries()

    max_tweets = 10000
    for date in dates:
        for query in queries:
            try:
                results = tweepy.Cursor(api.search, q=query,lang="es",show_user=True,include_entities=True,count=100,until=date).pages()
                tweet_count = 0
                for result in results:
                    t = int(time.time())
                    id = "{}_{}_{}".format(query.replace(" ",'_'),date,t)
                    file = 'nicaragua/{}.json'.format(id)

                    searched_tweets = [status._json for status in result]
                    logging.info("Searched {} result {} on {}".format(query,len(result),date))
                    print("Searched {} result {} on {}".format(query,len(result),date))
                    with open(file, 'w', encoding='utf8') as fp:
                        json.dump(searched_tweets, fp)

                    metadata = {'query':query,'date':date,'queried_time':t,"count":len(result)}
                    file_metadata = 'nicaragua/metadata/metadata_{}.json'.format(id)

                    with open(file_metadata, 'w', encoding='utf8') as fp:
                        json.dump(metadata, fp)

                    tweet_count = len(result) + tweet_count
                    if tweet_count > max_tweets:
                        print("Collected over {} tweets!".format(tweet_count))
                        break

            except TweepError as err:
                logging.info("Error occured for {} on {} - message: [{}]".format(query,date,err))

import os
import json
from pymongo.errors import BulkWriteError
from pymongo import MongoClient
from config import get_mongo_config

#db.tweets.createIndex({id:1},{unique:true})
#db.tweets.createIndex({id_str:1},{unique:true})
#db.history_file.createIndex({filename:1},{unique:true})

def list_twitter_files(basedir = './nicaragua/'):
    files = []
    objects = os.listdir(basedir)
    for file in objects:
        if file.endswith('.json'):
            files.append(basedir+'/'+file)
    return files

def open_twitter_json(file):
    file_name = os.path.basename(os.path.normpath(file))
    results = json.load(open(file))
    return results

def get_client():
    config = get_mongo_config()
    return MongoClient(config['host'], config['port'])

def inserted_file_list():
    db = get_client()['soyvandalo_test']
    history_file = db['history_file']
    files = history_file.find({})
    file_list = [f['filename'] for f in files]
    return file_list

def bulk_tweets(filename,tweet_results,metadata):
    db = get_client()['soyvandalo_test']
    tweets = db['tweets']
    tweet_metadata = db['tweet_metadata']
    history_file = db['history_file']
    try:
        result = tweets.insert_many(tweet_results,ordered=False)
        inserted_ids = result.inserted_ids
    except BulkWriteError as err:
        error_id = [ err_doc['op']['id'] for err_doc in err.details['writeErrors'] ]
        inserted_ids = [tweet['_id'] for tweet in tweet_results if tweet['id'] not in error_id]

    print('Tweets inserted {}'.format(len(inserted_ids)))

    #In case there are more than 1 inserted ids store the metadata aswell
    if len(inserted_ids) > 0:
        metadata['inserted_ids'] = inserted_ids
        tweet_metadata.insert(metadata)

    try:
        history_file.insert({'filename':filename})
    except BulkWriteError:
        pass

#./nicaragua_abril//#SOSNicaragua_#Nicaragua_2018-04-29_1525137835.json
def bulk_tweets_to_mongo(files=list_twitter_files()):
    filter_files = inserted_file_list()
    print(len(files))
    files = [f for f in files if f not in filter_files]
    print(len(files))
    for twitter_file in files:
        metadata_file = './nicaragua/metadata/metadata_{}'.format(os.path.basename(os.path.normpath(twitter_file)))
        twitter_results = open_twitter_json(twitter_file)
        metadata_result = json.load(open(metadata_file))
        print('Bulk insert {}'.format(twitter_file))
        bulk_tweets(twitter_file, twitter_results,metadata_result)



results = bulk_tweets_to_mongo()

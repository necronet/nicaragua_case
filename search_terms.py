import datetime
import random

queries = [
        'Lesther Aleman Dialogo',
        'Lesther Aleman Nicaragua',
        'Dialogo Nacional Nicaragua',
        'CIDH Nicaragua',
        'Esteli Nicaragua',
        'Sebaco Nicaragua',
        'Matagalpa Nicaragua',
        'Granada Nicaragua',
        '#SOSNicaragua #Nicaragua',
        "Ortega Nicaragua",
        "Protestas Nicaragua",
        "#Nicaragua UNAN",
        "POLICIA SOSNICARAGUA",
        "Policia Nicaragua",
        "JS Nicaragua",
        "Muerte estudiantes",
        "Desaparecidos Nicaragua",
        "#Nicaragua Saqueo",
        "#Nicaragua Juventud sandinistas",
        "Alvaro Conrado",
        "#AMiNoMeEngañaLaDerecha",
        "#NicaraguaQuierePaz",
        "#NoMasSaqueo",
        "#nomasviolenciacriminal",
        "#MRS Nicaragua",
        "#dialogotrabajoypaz",
        "#BRILLALAPAZ #NICARAGUAQUIEREPAZ",
        "#NicaraguaQuierePaz #DiálogoTrabajoyPaz"
        "#Noalavioencia #QueremoslaPaz #BrillaLaPaz",
        "#DIALOGOTRABAJOYPAZ #CADENASDEORACION #QueremoslaPaz",
        "#AMORANICARAGUA","#NICARAGUAAMOR #NICARAGUAREVOLUCION","#NICARAGUASANDINOVIVE"]

def get_queries():
    random.shuffle(queries)
    return queries

def get_dates(days=5):
    base = datetime.datetime.today()
    date_list = [base - datetime.timedelta(days=x) for x in range(0, days)]
    formatted_dates = [date_.strftime('%Y-%m-%d') for date_ in date_list]
    random.shuffle(formatted_dates)
    return formatted_dates

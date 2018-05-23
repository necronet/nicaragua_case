import datetime
import random

queries = [
        '#SOSNicaragua',
        'Lesther Aleman Dialogo',
        'Lesther Aleman Nicaragua',
        'Dialogo Nacional Nicaragua',
        'BLOCKTHESAPO',
        'Dialogo tranques',
        'Luis Andino UNEN',
        'Tranques Nicaragua',
        'CIDH Nicaragua',
        'Edwin Castro',
        'UPOLI piso',
        'CIDH masaya',
        'CIDH matagalpa',
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
        "Muerte estudiantes",
        "Desaparecidos Nicaragua",
        "#Nicaragua Saqueo",
        "#Nicaragua Juventud sandinistas",
        "#AMiNoMeEngañaLaDerecha",
        "#NicaraguaQuierePaz",
        "#NoMasSaqueo",
        '#NoMasTranques',
        '#VamosAlDialogo',
        '#EduardoSpiegeler',
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

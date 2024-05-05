import configparser
from notion_client import Client



def initialise_app():
    global client
    config = configparser.ConfigParser()
    config.read('./blog_dice/config.ini')
    api_key = config['DEFAULT']['API_KEY']
    client=Client(auth=api_key)
    return client

def get_DB_ID():
    global DB_ID_notion
    config = configparser.ConfigParser()#IDを取得（config.iniから
    config.read('./blog_dice/config.ini')
    DB_ID_notion = config['DB_ID']['DataBase_id']
    return DB_ID_notion

def LOG():
    global TXT_LOG
    TXT_LOG = 'history.log'
    return TXT_LOG

initialise_app()
get_DB_ID()
LOG()

# from blog_dice import client で導入

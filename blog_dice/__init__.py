import configparser
from notion_client import Client

def initialise_app():
    global client
    config = configparser.ConfigParser()
    config.read('./blog_dice/config.ini')
    api_key = config['DEFAULT']['API_KEY']
    client=Client(auth=api_key)
    return client

initialise_app()

# from blog_dice import client で導入

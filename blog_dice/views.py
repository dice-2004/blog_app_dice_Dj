from django.shortcuts import render
import configparser

# TXT_LOG = "history.log"
# config = configparser.ConfigParser()#IDを取得（config.iniから
# config.read('./config.ini')
# DB_ID_notion = config['DB_ID']['DataBase_id']

def frontpage(request):
    return render(request,"frontpage.html")

# def notion_detail(request,page_id):
#     #notionのページコンテンツ取得
#     #content =
#     return render(request,"notion.html")#{"content":content}

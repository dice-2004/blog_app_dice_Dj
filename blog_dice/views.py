from django.shortcuts import render,redirect
import configparser
from .my_module import notion,write_log
from . import DB_ID_notion,TXT_LOG
from django.views.generic import View

# TXT_LOG = "history.log"
# config = configparser.ConfigParser()#IDを取得（config.iniから
# config.read('./config.ini')
# DB_ID_notion = config['DB_ID']['DataBase_id']
class FrontpageView(View):

    def get(self,request):
        write_log.WriteLog(request.path,request.method,"connect web site.")
        contents,n = notion.get_filtered_pages(DB_ID_notion)
        print(*contents)
        return render(request,"frontpage.html",{"contents":contents})

class About_meView(View):
    def get(self,request):
        write_log.WriteLog(request.path,request.method,"connect web site.")
        return render(request,"about_me.html")

class ProductView(View):
    def get(self,request):
        write_log.WriteLog(request.path,request.method,"connect web site.")
        return render(request ,"product.html")

class Page_listView(View):
    def get(self,request):
        write_log.WriteLog(request.path,request.method,"connect web site.")
        contents,n = notion.get_filtered_pages(DB_ID_notion)
        print(*contents)
        return render(request,"page_list.html",{"contents":contents})

class Notion_detailView(View):
    def get(self,request,page_id):
        write_log.WriteLog(request.path,request.method,"connect web site.")
        #notionのページコンテンツ取得
        contents = notion.get_page_content(page_id)
        print(page_id)
        print(contents)
        return render(request,"notion_detail.html",{"contents":contents})

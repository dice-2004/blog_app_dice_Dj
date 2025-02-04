from django.shortcuts import render,redirect
import configparser
from .my_module import notion,write_log
from . import DB_ID_notion,TXT_LOG,ERROR_LOG
from django.views.generic import View
from logging import getLogger,DEBUG,FileHandler,ERROR,Formatter
import inspect
import json



# logger = getLogger(__name__)
# formatter = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')


# handler = FileHandler(TXT_LOG)
# handler.setLevel(DEBUG)
# handler.setFormatter(formatter)

# error_handler = FileHandler(ERROR_LOG)
# error_handler.setLevel(ERROR)
# error_handler.setFormatter(formatter)


# def try_do(func):#ログ未完了
#     function_name = inspect.currentframe().f_code.co_name
#     try:
#         logger.debug()
#         func()
#     except:
#         pass




class FrontpageView(View):

    def get(self,request):
        write_log.WriteLog(request.path,request.method,"connect web site.")
        contents = notion.get_filtered_pages(DB_ID_notion)
        # print(*contents)

        re=notion.get_page_content("9b89dcb8-3837-4e09-a1ac-02d92f5e14fc")
        # print(re)
        return render(request,"frontpage.html",{"contents":contents})




#POSTの[0]要素に識別番号を入れる
#serchなら1,categoryなら2

    def post(self,request):
        category=request.POST('xxx')

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
        contents = notion.get_filtered_pages(DB_ID_notion)
        # print(*contents)
        return render(request,"page_list.html",{"contents":contents,})

#POSTの[0]要素に識別番号を入れる
#serchなら1,categoryなら2,start_cursorなら3


    # def post(self,request):
    #     num=int(request.POST["count"])
    #     print(num)
    #     # category=request.POST('xxx')
    #     contents,n = notion.get_filtered_pages(database_id=DB_ID_notion,start_cursor=num)
    #     print(n)
    #     return render(request,"page_list.html",{"contents":contents,"n":n})


class Notion_detailView(View):
    def get(self,request,page_id):
        write_log.WriteLog(request.path,request.method,"connect web site.")
        #notionのページコンテンツ取得
        contents = notion.get_page_content(page_id)
        with open("contents.json", "w") as f:
            json.dump(contents, f, indent=4)
        last_update = notion.get_page_property_last_updated(page_id)
        # print(page_id)
        # print(contents)
        return render(request,"notion_detail.html",{"contents":contents,"last_update":last_update})

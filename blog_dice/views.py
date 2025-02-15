from django.shortcuts import render,redirect
import configparser
from .my_module import notion,write_log
from . import DB_ID_notion,TXT_LOG,ERROR_LOG
from django.views.generic import View
from logging import getLogger,DEBUG,FileHandler,ERROR,Formatter
import inspect
import json
import fcntl
import time
import datetime
from django.shortcuts import redirect





parent_page_id = "583d80de7fda49d1b493068ea10ad7a5"



# def open_pagelist(edit_time,param):

#     try:
#         with open("data/page_list.json", "r") as f:
#             page_list = json.load(f)
#         if edit_time== page_list["last_edit"]:
#             data=page_list["list"]
#             print("1")
#             return data
#         else:
#             data = notion.get_filtered_pages(database_id=DB_ID_notion,specific_category=param)
#             with open("data/page_list.json", "w") as f:
#                 json.dump({"last_edit":edit_time,"list":data}, f, indent=4)
#                 print("2")
#             return data
#     except :
#         data = notion.get_filtered_pages(database_id=DB_ID_notion,specific_category=param)
#         with open("data/page_list.json", "w") as f:

#             json.dump({"last_edit":edit_time,"list":data}, f, indent=4)
#             print("3")
#             return data


# def open_category(edit_time):
#     try:
#         with open("data/category.json", "r") as f:
#             category_list = json.load(f)
#         if edit_time== category_list["last_edit"]:
#             data = category_list["list"]
#             print("1")
#             return data
#         else:
#             data=notion.fetch_category(DB_ID_notion)
#             with open("data/category.json", "w") as f:
#                 json.dump({"last_edit":edit_time,"list":data}, f, indent=4)
#                 print("2")
#             return data
#     except :
#         data=notion.fetch_category(DB_ID_notion)
#         with open("data/category.json", "w") as f:
#             json.dump({"last_edit":edit_time,"list":data}, f, indent=4)
#             print("3")
#             return data

       # while True:
        #     try:
        #         with open("data/contents/"+page_id+".json", "r") as f:

        #             fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
        #             detail_list = json.load(f)
        #             contents = detail_list["list"]
        #             fcntl.flock(f, fcntl.LOCK_UN)
        #         break
        #     except BlockingIOError:
        #         time.sleep(1)
# f.seek(0)
#             json.dump(data, f, ensure_ascii=False, indent=4)
#             f.truncate()

def save_data(request):
    # ページリスト
    dt_now = datetime.datetime.now()
    time =dt_now.strftime('%Y/%m/%d/ %H:%M')
    page=notion.get_filtered_pages(database_id=DB_ID_notion)
    while True:
        try:
            with open("data/page_list.json", "w") as f:
                fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
                f.seek(0)
                json.dump({"last_edit":time,"list":page}, f, indent=4)
                f.truncate()
                fcntl.flock(f, fcntl.LOCK_UN)
            break
        except BlockingIOError:
            time.sleep(1)

    # カテゴリー
    category = notion.fetch_category(DB_ID_notion)
    while True:
        try:
            with open("data/category.json", "w") as f:
                fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
                f.seek(0)
                json.dump({"last_edit":time,"list":category}, f, indent=4)
                f.truncate()
                fcntl.flock(f, fcntl.LOCK_UN)
            break
        except BlockingIOError:
            time.sleep(1)


    page_id =[x["page_id"] for x in page]
    edit_time = [x["Last_updated"] for x in page]
    for p_id,e_time in zip(page_id,edit_time):
        trash=open_detail(e_time,p_id)
    return redirect('https://www.notion.so/583d80de7fda49d1b493068ea10ad7a5')  # 外部サイトへリダイレクト
    # return render(request,"load.html")


def open_detail(edit_time,page_id):
    try:
        while True:
            try:
                with open("data/contents/"+page_id+".json", "r") as f:
                    fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
                    detail_list = json.load(f)
                    fcntl.flock(f, fcntl.LOCK_UN)
                break
            except BlockingIOError:
                time.sleep(1)
        if edit_time== detail_list["last_edit"]:
            data = detail_list["list"]
            print("1")
            return data
        else:
            data= notion.get_page_content(page_id)
            while True:
                try:
                    with open("data/contents/"+page_id+".json", "w") as f:
                        fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
                        f.seek(0)
                        json.dump({"last_edit":edit_time,"list":data}, f, indent=4)
                        f.truncate()
                        fcntl.flock(f, fcntl.LOCK_UN)
                    break
                except BlockingIOError:
                    time.sleep(1)
            return data
    except :
        data= notion.get_page_content(page_id)
        while True:
            try:
                with open("data/contents/"+page_id+".json", "w") as f:
                    fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
                    f.seek(0)
                    json.dump({"last_edit":edit_time,"list":data}, f, indent=4)
                    f.truncate()
                    fcntl.flock(f, fcntl.LOCK_UN)
                break
            except BlockingIOError:
                time.sleep(1)
        return data



class FrontpageView(View):

    def get(self,request):
        write_log.WriteLog(request.path,request.method,"connect web site.")
        return render(request,"frontpage.html")




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
        try:
            param = request.GET.get('param')
        except:
            param = None

        write_log.WriteLog(request.path,request.method,"connect web site.")

        # last_edit=notion.get_edit_db(parent_page_id)
        # contents = notion.get_filtered_pages(database_id=DB_ID_notion,specific_category=param)
        # category = notion.fetch_category(DB_ID_notion)

        # ファイルロッキングシステム
        while True:
            try:
                with open("data/page_list.json", "r") as f:
                    fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
                    page_list = json.load(f)
                    page_list = page_list["list"]
                    fcntl.flock(f, fcntl.LOCK_UN)
                break
            except BlockingIOError:
                time.sleep(1)

        while True:
            try:
                with open("data/category.json", "r") as f:
                    fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
                    category_list = json.load(f)
                    category = category_list["list"]
                    fcntl.flock(f, fcntl.LOCK_UN)
                break
            except BlockingIOError:
                time.sleep(1)
        if param == None:
            contents = page_list
        else:
            contents = []
            for page in page_list:
                if param in page["category"]:
                    contents.append(page)


        return render(request,"page_list.html",{"contents":contents,"category":category})


class Notion_detailView(View):
    def get(self,request,page_id):
        write_log.WriteLog(request.path,request.method,"connect web site.")
        #notionのページコンテンツ取得
        title = request.GET.get('title', '')
        last_edit = request.GET.get('last_edit','')
        contents = open_detail(last_edit,page_id)
        with open("contents.json", "w") as f:
            json.dump(contents, f, indent=4)
        return render(request,"notion_detail.html",{"contents":contents,"title":title})

class LoadAllView(View):
    def get(self,request):
        return save_data(request)

    def post(self,request,*args, **kwargs):
        return save_data(request)


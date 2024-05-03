from django.urls import path
from . import views


app_name = 'blog_dice'
TXT_LOG = "history.log"

urlpatterns = [
    path("",views.frontpage ,name = 'frontpage'),
    # path("notion/<str:page_id>",notion_detail,name = "notion_detail")
]

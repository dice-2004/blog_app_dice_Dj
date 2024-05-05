from django.urls import path
from . import views


app_name = 'blog_dice'
TXT_LOG = "history.log"

urlpatterns = [
    path("",views.frontpage ,name = 'frontpage'),
    path("about_me",views.about_me ,name='about_me'),
    path("product",views.product ,name="product"),
    path("page_list",views.page_list ,name = 'page_list'),
    path("notion/<page_id>",views.notion_detail ,name = "notion_detail"),
    path("notion",views.frontpage ,name = 'frontpage'),
]

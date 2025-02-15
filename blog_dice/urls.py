from django.urls import path
from . import views


app_name = 'blog_dice'
TXT_LOG = "history.log"

urlpatterns = [
    path("",views.FrontpageView.as_view() ,name = 'frontpage'),
    path("notion",views.FrontpageView.as_view() ,name = 'frontpage'),
    path("about_me",views.About_meView.as_view() ,name='about_me'),
    path("product",views.ProductView.as_view() ,name="product"),
    path("page_list",views.Page_listView.as_view() ,name = 'page_list'),
    path("notion/<page_id>",views.Notion_detailView.as_view() ,name = "notion_detail"),
    path("this/page/is/load/all/my/page/detail/So/you/should/jump/my/top",views.LoadAllView.as_view() ,name = 'load_all'),
]

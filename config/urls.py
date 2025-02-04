from django.contrib import admin
from django.urls import path
from django.urls import path, include
from . import top

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",top.top),
    path('blog_dice/',include('blog_dice.urls'),name='tops'),
]

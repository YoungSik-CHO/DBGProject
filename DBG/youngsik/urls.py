from django.urls import path
from django.urls.conf import include
from . import views #.은 현재폴더의 디렉토리라는뜻. 즉 현재폴더의 views.py를 import하는것임
from .views import blog_home

urlpatterns = [
    path('', views.index),  #위의 urls.py와는 달리 include가 없음
    path('blog/', views.blog_home)
]
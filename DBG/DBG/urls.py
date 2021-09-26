from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('youngsik/', include('youngsik.urls')), #elections app을 include 해주는것임.
    path('kyusung/', include('kyusung.urls')), #elections app을 include 해주는것임.
    path('jingyu/', include('jingyu.urls')), #elections app을 include 해주는것임.

]

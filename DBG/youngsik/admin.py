from django.contrib import admin
# 생성한 model을 admin.py에서 import
from .models import Category, Articles 
# Register your models here.

# 생성한 model을 관리자 페이지에서 제어 가능하도록 등록
admin.site.register(Category)
admin.site.register(Articles)
from django.db import models

## 생성하고자 하는 model을 생성 후
## manage.py 경로에서 python manage.py makemigrations , python manage.py migrate를 실행하면
## 생성한 model을 담을 수 있는 데이터 공간이 만들어짐


# Create your models here.
# Board
class Category(models.Model):
    # 제목
    name = models.CharField(max_length=255)
    # 내용
    description = models.CharField(max_length=500)

# Articles
class Articles(models.Model):
    # Categories
    categories = models.ManyToManyField(Category, blank=True)
    # name
    name = models.CharField(max_length=500)
    #description
    description = models.CharField(max_length=500)
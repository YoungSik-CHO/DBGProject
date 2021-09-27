from django.shortcuts import render
from django.http import HttpResponse
from .models import Articles

# Create your views here.
def index(request):
    return HttpResponse("Hello Youngsik!")

# blog_home
def blog_home(request):
    article_list = Articles.objects.all()
    context = {'article_list' : article_list}
    return render(request, 'index.html', context)
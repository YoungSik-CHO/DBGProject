from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello Kyusung!")

def test(request):
    return HttpResponse("Hi test01")
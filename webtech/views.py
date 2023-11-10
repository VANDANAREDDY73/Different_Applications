from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def html(request):
  return HttpResponse('<h1>Html Used for Creating Webpages<h1>')
def css(request):
  return render(request,'css.html')


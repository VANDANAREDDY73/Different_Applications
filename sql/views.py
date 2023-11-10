from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def joins(request):
  return HttpResponse('<h1>SQL Joins<h1><br><h2>Inner Join ,Outer Join ,Full outer Join')
def commands(request):
  return render(request,'commands.html')
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def functions(request):
  return HttpResponse('<h1>There are two types of functions in python</h1><br><h2>Built in functions</h2><br><h2>User Defined functions</h2>')
def oops(request):
  return render(request,'oops.html')

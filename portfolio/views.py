from django.http import HttpResponse
from django.shortcuts import render
import operator
def resume(request):
    return render(request,'resume.html')

def index(request):
    return render(request,'index.html')

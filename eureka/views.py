from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    return HttpResponseRedirect('index')

def welcome(request):
    return render(request, 'index.html')

def showAboutPage(request):
    return render(request, 'about.html')

def showHowWorks(request):
    return render(request, 'howitworks.html')

def showExplore(request):
    return render(request, 'explore.html')

def showAProject(request):
    return render(request, 'singleproject.html')

def startProject(request):
    return render(request, 'startproject.html')

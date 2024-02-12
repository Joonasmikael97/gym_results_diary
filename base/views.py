from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('Home page')

def resultdiary(request):
    return HttpResponse('Gym results')

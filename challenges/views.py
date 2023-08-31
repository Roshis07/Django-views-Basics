from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def january1(request):
    return HttpResponse("Hi this is january month after all.")
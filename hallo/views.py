from django.shortcuts import render
from django.http import HttpResponse
def hallo(request):
    return HttpResponse("Hallo Welt!")
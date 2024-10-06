from django.shortcuts import render
from django.http import HttpResponse
def hallo(request):
    return render(request, 'hallo.html')
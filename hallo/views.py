from django.shortcuts import render
def hallo(request):
    return render(request, 'index.html')
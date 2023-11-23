from django.shortcuts import render
from django.http import HttpResponse

def indice(request):
    return render(request, '../templates/extranet/index.html')

# Create your views here.
def indice2(request):
    return render(request, '../templates/extranet/baseExtranet.html')

def indice3(request):
    return render(request, '../templates/content/local1.html')

def indice4(request):
    return render(request, '../templates/content/local2.html')

def indice5(request):
    return render(request, '../templates/content/local3.html')


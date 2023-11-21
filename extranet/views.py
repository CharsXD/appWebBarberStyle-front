from django.shortcuts import render
from django.http import HttpResponse

def indice(request):
    return render(request, '../templates/extranet/index.html')

# Create your views here.
def indice2(request):
    return render(request, '../templates/extranet/baseExtranet.html')

def indice3(request):
    return render(request, '../templates/footersYHeaders/copiadero.html')
from django.shortcuts import render

def index(request):
    return render(request, 'xmlvalidator/index.html')

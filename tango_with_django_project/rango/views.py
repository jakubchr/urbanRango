from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}

    return render(request, 'index.html', context=context_dict)

def about(request):
    response = HttpResponse()
    response.write("<h1> About </h1>")
    response.write("<p> This is about page </p>")
    response.write("<a href='/rango/'> Back </a>")
    return response
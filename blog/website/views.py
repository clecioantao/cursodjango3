from django.http import HttpResponse
from django.shortcuts import render

def hello_blog(request):
    lista = ['lista','lista2','lista3','lista4','Django']
    data = {'name': 'Curso Django', 'lista_tec': lista}
    
    return render(request, 'index.html', data)


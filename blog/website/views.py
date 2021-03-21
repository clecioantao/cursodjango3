from django.http import HttpResponse
from django.shortcuts import render
from .models import Post


def hello_blog(request):
    
    lista = ['lista','lista2','lista3','lista4','Django']
    
    #list_posts = Post.objects.all() # busca dados model Posts
    list_posts = Post.objects.filter(approved=True)
    
    # dicionario com dados
    data = {
        'name': 'Curso Django', 
        'lista_tec': lista, 
        'posts': list_posts
        }
      
    return render(request, 'index.html', data)

def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post_detail.html', {'post': post})
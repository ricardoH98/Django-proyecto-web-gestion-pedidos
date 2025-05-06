from django.shortcuts import render
from .models import Post, Categoria

# Create your views here.

def blog(request):
    categorias = Categoria.objects.all()
    posts = Post.objects.all()

    return render(request, 'blog.html', {'posts': posts, 'categorias': categorias})

def categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    posts = Post.objects.filter(categorias=categoria)

    return render(request, 'categoria.html', {'categoria': categoria, 'posts': posts})
from django.shortcuts import render

from .models import Categoria, Mensagem, Tag


def index(request):
    mensagens = Mensagem.objects.all()
    categorias = Categoria.objects.all()
    tags = Tag.objects.all()
    return render(request, "home/index.html", {
        "mensagens": mensagens,
        "categorias": categorias,
        "tags": tags,
    })


def sobre(request):
    return render(request, "home/sobre.html")
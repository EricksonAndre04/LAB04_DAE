from django.shortcuts import render
from .models import Entrada
from .models import Autor


def lista_entradas(request):
    entradas = Entrada.objects.all()
    return render(request, 'blog/lista_entradas.html', {'entradas': entradas})

def filtro_entradas(request,autor):
    autor=Autor.objects.get(nombre=autor)
    entradas=Entrada.objects.filter(autor=autor)
    context={
        'autor':autor,
        'entradas':entradas
    }
    return render(request,'blog/filtro_entradas.html',context)
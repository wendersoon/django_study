from django.shortcuts import render, get_object_or_404
from .models import Produto

# Create your views here.

def index(request):
    produtos = Produto.objects.all()    
    context = {
        'Aluno': 'Batman',
        'Curso': 'Das Trevas',
        'Grau': 'Cavaleiro',
        'produtos': produtos,
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')

def produto(request, id):
    # prod = Produto.objects.get(id=id)
    prod = get_object_or_404(Produto, id=id)
    context = {
        'produto': prod,
    }
    return render(request, 'produto.html', context)

def error404(request, exception):
    return render(request, '404.html')
from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'Aluno': 'Batman',
        'Curso': 'Das Trevas',
        'Grau': 'Cavaleiro'
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')
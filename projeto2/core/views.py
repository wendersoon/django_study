from django.shortcuts import render
from django.contrib import messages

from .forms import ContatoForm, ProdutoModelForm

def index(request):
    return render(request, 'index.html')

def contato(request):
    form = ContatoForm(request.POST or None)
    
    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_email()
            
            messages.success(request, 'E-mail enviado com sucesso!')
            form = ContatoForm()

        else:
            messages.error('Não foi Enviado!')
    context = {
        'form': form
    }
    return render(request, 'contato.html', context=context)

def produto(request):
    
    if str(request.method) == 'POST':
        form = ProdutoModelForm(request.POST)
        if form.is_valid():
            form.save()
            
            messages.success(request, 'Produto salvo com sucesso')
        else:
            messages.error(request, 'Erro ao salvar produto.')
    else:
        form = ProdutoModelForm()
    
    form = ProdutoModelForm()
    context = {
        'form': form
    }
    
    return render(request, 'produto.html', context=context)
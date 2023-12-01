from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext as _
from django.utils import translation


from .models import Servico, Equipe, Features
from .forms import ContactForm

class IndexView(FormView):
    template_name = 'index.html'
    form_class=ContactForm
    success_url= reverse_lazy('index')

    def get_context_data(self, **kwargs):
        
        context = super(IndexView, self).get_context_data(**kwargs)
        lang = translation.get_language() # obtém a lingua atráves do navegador e coloca na variável
        context['servicos'] = Servico.objects.order_by('?').all()
        context['equipes'] = Equipe.objects.order_by('?').all()
        context['features'] = Features.objects.all()
        context['lang'] = lang
        translation.activate(lang)     # a variável de contexto é para adicionar no html
        
        return context
    
    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, _('Email enviado com sucesso'))
        return super(IndexView, self).form_valid(form,  *args, **kwargs)
    
    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, _('Erro ao enviar email'))
        return super(IndexView, self).form_invalid(form, *args, **kwargs)
    
    
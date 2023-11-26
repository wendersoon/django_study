from django import forms
from django.core.mail.message import EmailMessage
from django.utils.translation import gettext_lazy as _  ## Esse é o recomendado para forms e models

class ContactForm(forms.Form):
    nome = forms.CharField(label=_('Nome'), max_length=100)
    email = forms.EmailField(label=_('Email'),max_length=100)
    assunto = forms.CharField(label=_('Assunto'), max_length=100)
    mensagem = forms.CharField(label=_('Mensagem'))
    
    def send_mail(self):
        nome = self.cleaned_data.get('nome')
        email = self.cleaned_data.get('email')
        assunto = self.cleaned_data.get('assunto')
        mensagem = self.cleaned_data.get('mensagem')
        
        conteudo = f'Nome: {nome}\nEmail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'
         
        msg = EmailMessage(
            subject=assunto,
            body=conteudo,
            from_email='contato@fusion.com.br',
            to=['contato@fusion.com.br',],
            headers={'Replay-To': email},
        )
        msg.send()
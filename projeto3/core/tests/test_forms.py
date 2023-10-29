from django.test import TestCase
from model_mommy import mommy

from core.forms import ContactForm


class ContactFormTest(TestCase):
    
    def setUp(self):
        self.nome = 'Wenderson'
        self.assunto = "python"
        self.email = 'teste@gmail.com'
        self.mensagem = 'teste'
        
        self.dados = {
            'nome': self.nome,
            'assunto': self.assunto,
            'email': self.email,
            'mensagem': self.mensagem,
        }
        
        self.form = ContactForm(data=self.dados) # é a mesma coisa quando se faz ContactForm(request.POST)
        
    def test_send_email(self):
        form1 = ContactForm(data=self.dados)
        form1.is_valid()
        res1 = form1.send_mail()
        
        form2 = self.form
        form2.is_valid()
        res2 = form2.send_mail()
        
        self.assertEqual(res1, res2)
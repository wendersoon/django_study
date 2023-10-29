from django.test import TestCase, Client
from django.urls import reverse_lazy

from core.views import IndexView

class IndexViewTest(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.response = self.client.get(reverse_lazy('index'))
        
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

        self.cliente = Client()
        
    def test_form_valid(self):
        request = self.cliente.post(reverse_lazy('index'), data=self.dados)
        self.assertEqual(request.status_code, 302)
            
    def test_form_invalid(self):
        dados ={
            'nome': self.nome,
            'assunto': self.assunto,
            'email': self.email,
        }
    
        request = self.cliente.post(reverse_lazy('index'), data=dados)
        self.assertEqual(request.status_code, 200)
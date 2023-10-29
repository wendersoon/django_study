import uuid
from django.test import TestCase
from model_mommy import mommy

from core.models import get_file_path, Servico, Equipe, Cargo

class GetFilePathTestCase(TestCase):
    
    def setUp(self):
        self.filename = f'{uuid.uuid4()}.png'
        
    def test_get_file_path(self):
        arquivo = get_file_path(None, 'teste.png')
        self.assertTrue(len(arquivo), len(self.filename))
        
class ServicoTestCase(TestCase):
    
    def setUp(self):
        self.servico = mommy.make(Servico)
        
    def test_str(self):
        self.assertEqual(str(self.servico), self.servico.servico)
        
class EquipeTestCase(TestCase):
    
    def setUp(self):
        self.equipe = mommy.make(Equipe)
        
    def test_str(self):
        self.assertEqual(str(self.equipe), self.equipe.nome)
        
class CargoTestCase(TestCase):
    
    def setUp(self):
        self.cargo = mommy.make(Cargo)
        
    def test_str(self):
        self.assertEqual(str(self.cargo), self.cargo.cargo)

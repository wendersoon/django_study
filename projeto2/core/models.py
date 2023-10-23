from django.db import models

# SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify

class Base(models.Model):
    criado = models.DateField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)
    
    class Meta:
        abstract = True
        
class Produto(Base):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    estoque = models.IntegerField('Estoque')
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)
    
    def __str__(self):
        return self.nome   
    
    
def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance)
    
signals.pre_save.connect(produto_pre_save, sender=Produto)
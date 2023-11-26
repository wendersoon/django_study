import uuid
from django.db import models
from stdimage  import StdImageField
from django.utils.translation import gettext_lazy as _  ## Esse é o recomendado para forms e models


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

#classe abstrata
class Base(models.Model):
    criados = models.DateField(_('Criação'), auto_now_add=True)
    modificado = models.DateField(_('Atualização'), auto_now=True)
    ativo = models.BooleanField(_('Ativo'), default=True)
    
    class Meta:
        abstract = True
        
class Servico(Base):
    ICONE_CHOICES =(
        ('lni-cog', _("Engrenagem")),
        ('lni-stats-up', _("Gráfico")),
        ('lni-users', _("Usuários")),
        ('lni-layers', _("Design")),
        ('lni-mobile', _("Mobile")),
        ('lni-rocket', _("Foguete")),
    )
    
    servico = models.CharField(_('Serviço'), max_length=100)
    descricao = models.TextField(_('Descricao'), max_length=200)
    icone = models.CharField(_('Icone'), max_length=12, choices=ICONE_CHOICES)
    
    class Meta:
        verbose_name = _('Serviço')
        verbose_name_plural = _('Serviços') 
        
    def __str__(self) -> str:
        return self.servico
    
class Cargo(Base):
    cargo = models.CharField(_('Cargo'), max_length=100)
    
    class Meta:
        verbose_name = _('Cargo')
        verbose_name_plural = _('Cargos')
        
    def __str__(self):
        return self.cargo
    
class Equipe(Base):
    nome = models.CharField(_('Nome'), max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField(_('Bio'), max_length=200)
    imagem = StdImageField(_('Imagem'), upload_to=get_file_path, variations={'thumb':{'width': 480, 'height': 480, 'crop':True}})
    facebook = models.CharField(_('Facebook'), max_length=100, default='#')
    twitter = models.CharField(_('Twitter'), max_length=100, default='#')
    instagram = models.CharField(_('Instagram'), max_length=100, default='#')
    
    class Meta:
        verbose_name = _('Equipe')
        verbose_name_plural = _('Equipe')
        
    def __str__(self):
        return self.nome
    
class Features(Base):
    ICONE_CHOICES =(
        ('lni-cog', _("Engrenagem")),
        ('lni-leaf', _("Folha")),
        ('lni-layers', _("Design")),
        ('lni-laptop-phone', _("Computador e Celular")),
        ('lni-rocket', _("Foguete")),
    )
    
    feature = models.CharField(_('Feature'), max_length=100)
    descricao = models.CharField(_('Descricao'), max_length=200)
    icone = models.CharField(_('Icone'), max_length=16, choices=ICONE_CHOICES)

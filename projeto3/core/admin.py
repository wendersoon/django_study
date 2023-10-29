from django.contrib import admin

from .models import Cargo, Servico, Equipe, Features

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'modificado')
    
@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'descricao', 'icone', 'ativo','modificado')
    
@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'bio', 'imagem', 'facebook', 'twitter', 'instagram', 'ativo','modificado')
    
@admin.register(Features)
class FeaturesAdmin(admin.ModelAdmin):
    list_display = ('feature', 'descricao', 'icone', 'ativo','modificado')
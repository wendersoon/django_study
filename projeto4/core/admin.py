from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', '_autor')
    exclude = ['author']
    
    def _autor(self, instance):
        return f'{instance.autor.get_full_name()}'
    
    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        qs = qs.filter(autor=request.user)
        
    def save_model(self, request, obj, form, change):
        obj.autor = request.user
        return super().save_model(request, obj, form, change)
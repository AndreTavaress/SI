from django.contrib import admin
from receitas.models import *

@admin.register(receita)
class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('ingredientes', 'receita_criada')

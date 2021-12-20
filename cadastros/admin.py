from django.contrib import admin
from .models import Campo, Atividade, Campus 

@admin.register(Campo)
class CampoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'criado', 'atualizado', 'ativo')

@admin.register(Atividade)
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('numero', 'descricao', 'pontos', 'detalhes', 'criado', 'atualizado', 'ativo')

@admin.register(Campus)
class CampusAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade', 'telefone', 'criado', 'atualizado', 'ativo')


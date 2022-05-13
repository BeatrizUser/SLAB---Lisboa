from django.contrib import admin
from .models import Cadastro, calc_idade

@admin.register(Cadastro)
class CadastroAdmin(admin.ModelAdmin):
	list_display = ("nome_completo_aluno", "created",)
	prepopulated_fields = {"slug": ("nome_completo_aluno",)}
	#prepopulated_fields = {"idade": (calc_idade(Cadastro.data_de_Nascimento_do_Aluno),)}
	
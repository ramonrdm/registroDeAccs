# -*- coding: utf-8 -*-
from django.contrib import admin
from aaccs.models import AACC, Aluno

class AACCAdmin(admin.ModelAdmin):
	search_fields = ['titulo']
	autocomplete_fields = ['aluno']


class AlunoAdmin(admin.ModelAdmin):
	search_fields = ['nome']


admin.site.register(AACC, AACCAdmin)
admin.site.register(Aluno, AlunoAdmin)

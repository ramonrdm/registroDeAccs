# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Acc, Aluno

class AccAdmin(admin.ModelAdmin):
	search_fields = ['titulo']


class AlunoAdmin(admin.ModelAdmin):
	search_fields = ['nome']



admin.site.register(Acc, AccAdmin)
admin.site.register(Aluno, AlunoAdmin)

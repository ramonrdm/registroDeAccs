# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Acc(models.Model):
	titulo = models.CharField(max_length=200)
	aluno = models.CharField(max_length=200)
	matricula = models.CharField(max_length=200)
	email = models.EmailField()
	carga_horaria = models.CharField(max_length=200)
	instituicao = models.CharField(max_length=200)
	local = models.CharField(max_length=200)
	data_do_curso = models.DateField()
	data_de_emissao = models.DateField()
	responsavel = models.CharField(max_length=200)
	relatorio = models.TextField()
	#arquivo_anexado = 
	#tipo_atividade = 
	#ISSN_ou_ISBN =
	#link_externo = 

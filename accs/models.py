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
	arquivo_anexado = models.FileField(default=None, blank=True)
	link_externo = models.CharField(max_length=200, default=None)

	ensino_a_distancia = 'EaD'
	tipo_atividade_choices = (
		('EaD', 'Ensino a Distância'),
		('PR', 'Presencial'),
	)
	tipo_atividade = models.CharField(max_length=200, choices=tipo_atividade_choices, default=ensino_a_distancia)
	
	"""
	ISSN = 'ISSN'
	ISBN = 'ISBN'

	codigo_publicacao_choices = (
		('ISSN', 'ISSN'),
		('ISBN', 'ISBN')
	)
	codigo_publicacao_tipo = models.CharField(max_length=200, choices=codigo_publicacao_choices, default=ISSN)
	codigo_publicacao_numero = models.CharField(max_length=200, default=None)
	"""
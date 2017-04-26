# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Aluno(models.Model):
	matricula = models.IntegerField()
	email = models.EmailField()
	nome = models.CharField(max_length=255)

class Acc(models.Model):
	titulo = models.CharField(max_length=200)
	aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
	carga_horaria = models.CharField(max_length=200)
	instituicao = models.CharField(max_length=200)
	local = models.CharField(max_length=200)
	data_do_curso = models.DateField()
	data_de_emissao = models.DateField()
	relatorio = models.TextField()
	arquivo_anexado = models.FileField(default=None, blank=True)
	link_externo = models.CharField(max_length=200, blank=True)
	usuario = models.ForeignKey(User,default = 1)

	ensino_a_distancia = 'EaD'
	tipo_atividade_choices = (
		('EaD', 'Ensino a Distância'),
		('PR', 'Presencial'),
	)
	tipo_atividade = models.CharField(max_length=200, choices=tipo_atividade_choices, default=ensino_a_distancia)
	
	codigo_de_publicacao_choices = (
		('ISSN', 'ISSN'),
		('ISBN', 'ISBN')
	)
	codigo_de_publicacao_tipo = models.CharField(max_length=200, choices=codigo_de_publicacao_choices, default='ISSN')
	codigo_de_publicacao = models.CharField(max_length=200)



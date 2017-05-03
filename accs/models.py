# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Aluno(models.Model):
	matricula = models.IntegerField()
	email = models.EmailField()
	nome = models.CharField(max_length=200)

	def __str__(self):
		return self.nome

class Acc(models.Model):
	titulo = models.CharField(max_length=200)
	aluno = models.ForeignKey(Aluno)
	cargaHoraria = models.DecimalField(decimal_places=1, max_digits=200)
	instituicao = models.CharField(max_length=200)
	local = models.CharField(max_length=200)
	dataCurso = models.DateField()
	dataEmissao = models.DateField()
	relatorio = models.TextField(blank = True)
	anexo = models.FileField(default=None, blank=True)
	linkExterno = models.CharField(max_length=200, blank=True)
	usuario = models.ForeignKey(User,default = 1)


	tipoAtividadeChoices = (
		('1a', 'Eventos - Participação'),
		('1b', 'Eventos - Apresentação de trabalho'),
		('1c', 'Eventos - Interpretação'),
		('1d', 'Eventos - Organização'),
		('2a', 'Defesas - Participação'),
		('2b', 'Defesas - Interpretação'),
		('3a', 'Pesquisa - Participação como pesquisador'),
		('3b', 'Pesquisa - Participação como contribuidor de dados'),
		('4a', 'Extensão - Participação em projetos'),
		('4b', 'Extensão - Participação como aluno'),
		('4b', 'Extensão - Participação como especialista'), #Conferir numero da atividade
		('5a', 'Ensino - Monitoria em Letras-Libras'),
		('5b', 'Ensino - Docência em Libras'),
		('6a', 'Publicação - Resumos'),
		('6b', 'Publicação - Artigos completos'),
		('6b', 'Publicação - Material didático'), #Conferir numero da atividade
		('7a', 'Atividades culturais - Participação'),
		('7b', 'Atividades culturais - Atuação'),
	)
	tipoAtividade = models.CharField(max_length=200, choices=tipoAtividadeChoices, default=tipoAtividadeChoices[0])
	
	ISSN = models.IntegerField(blank=True, null = True)
	ISBN = models.IntegerField(blank=True, null = True)

	def clean(self):
		if self.ISSN == None and self.ISBN == None:
			raise ValidationError('Preencha pelo menos algum dos dois campos')

	def __str__(self):
		return "Certificado do " + self.aluno.nome + " sobre " + self.titulo
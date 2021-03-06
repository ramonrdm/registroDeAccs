# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Aluno(models.Model):
	matricula = models.IntegerField("Matrícula", unique=True)
	email = models.EmailField("E-mail")
	nome = models.CharField(max_length=200)

	def __str__(self):
		return self.nome

class AACC(models.Model):
	titulo = models.CharField("Título", max_length=200)
	aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
	cargaHoraria = models.DecimalField("Carga horária",decimal_places=1, max_digits=200)
	instituicao = models.CharField("Instituição", max_length=200)
	local = models.CharField(max_length=200)
	dataCurso = models.DateField("Data do curso")
	dataEmissao = models.DateField("Data de emissão")
	relatorio = models.TextField("Relatório", blank=True)
	anexo = models.FileField(default=None, blank=True)
	linkExterno = models.CharField("Link externo",max_length=200, blank=True)
	usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuário",default = 1)


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
			raise ValidationError('ISSN ou ISBN devem ser preenchidos.')
		if self.dataCurso > self.dataEmissao:
			raise ValidationError('A data de emissão do certificado deve ser posterior a de início do curso.')

	def __str__(self):
		return "Certificado do " + self.aluno.nome + " sobre " + self.titulo
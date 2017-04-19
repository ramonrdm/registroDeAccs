# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Acc(models.Model):
	titulo = models.CharField(max_length=200)
	aluno = models.CharField(max_length=200)
	horas = models.CharField(max_length=200)

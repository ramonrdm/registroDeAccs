# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from .models import Acc, Aluno
from forms import FormAcc, FormSearch
from django.core.exceptions import ObjectDoesNotExist

def index(request):
	if request.method == 'POST':
		form = FormSearch(request.POST)
		#if form.is_valid():
		dados = form.data
		busca = dados['busca']
		try:
			resultado = Acc.objects.filter(aluno = Aluno.objects.filter(nome__icontains=busca))
		except ObjectDoesNotExist:
			resultado = []
		if(len(resultado) == 0):
			try:
				resultado = Acc.objects.filter(aluno=Aluno.objects.filter(matricula__icontains = busca))
			except BaseException:
				resultado = []
		context = {"itens":resultado,"form":FormSearch()}
		return render(request, 'index.html', context)
	else:
		resultado = []
		context = {"itens":resultado,"form":FormSearch()}
		return render(request, 'index.html', context)

def item(request, item_id):
	item = get_object_or_404(Acc, id=item_id)
	return render(request, 'item.html', {'item': item})
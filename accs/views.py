# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from .models import Acc, Aluno
from forms import FormAcc, FormSearch
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q

def index(request):
	if request.method == 'POST':
		form = FormSearch(request.POST)
		dados = form.data
		busca = dados['busca']
		resultado = Acc.objects.filter(Q(aluno__nome__icontains=busca) | Q(aluno__matricula__icontains=busca))
		context = {"itens":resultado,"form":FormSearch()}
		return render(request, 'index.html', context)
	else:
		resultado = []
		context = {"itens":resultado,"form":FormSearch()}
		return render(request, 'index.html', context)

def item(request, item_id):
	item = get_object_or_404(Acc, id=item_id)
	return render(request, 'item.html', {'item': item})
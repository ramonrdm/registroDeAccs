# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from .models import Acc, Aluno
from forms import FormAcc, FormSearch
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q

def index(request):
	if request.method == 'POST':
		post = True;
		form = FormSearch(request.POST)
		resultado = Acc.objects.filter(Q(aluno__nome__icontains=form.data['busca']) | Q(aluno__matricula__icontains=form.data['busca']))
		return render(request, 'index.html', {"post":post,"itens":resultado,"form":FormSearch()})
	else:
		post = False
		resultado = []
		return render(request, 'index.html', {"post":post,"itens":resultado,"form":FormSearch()})

def item(request, item_id):
	item = get_object_or_404(Acc, id=item_id)
	return render(request, 'item.html', {'item': item})
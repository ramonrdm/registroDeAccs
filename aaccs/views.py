# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from aaccs.models import AACC, Aluno
from aaccs.forms import FormAACC, FormSearch
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q

def index(request):
	if request.method == 'POST':
		form = FormSearch(request.POST)
		resultado = AACC.objects.filter(Q(aluno__nome__icontains=form.data['busca']) | Q(aluno__matricula__icontains=form.data['busca']))
		return render(request, 'index.html', {"itens":resultado,"form":FormSearch()})
	else:
		return render(request, 'index.html', {"itens":[],"form":FormSearch()})

def item(request, item_id):
	item = get_object_or_404(AACC, id=item_id)
	return render(request, 'item.html', {'item': item})
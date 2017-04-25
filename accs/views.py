# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

from .models import Acc

from forms import FormAcc

def index(request):
	accList = Acc.objects.all()
	context = {'accList': accList}
	return render(request, 'index.html', context)

def adiciona(request):
	if request.method == 'POST':
		form = FormAcc(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'salvo.html', {})
		return render(request, 'adiciona.html', {'form': form})
	else:
		form = FormAcc()
		return render(request, 'adiciona.html', {'form': form})

def item(request, item_id):
	item = get_object_or_404(Acc, id=item_id)
	if request.method == 'POST':
		form = FormAcc(request.POST, instance = item)
		if form.is_valid():
			form.save()
			return render(request, 'salvo.html', {})
		return render(request, 'item.html', {'form': form})
	else:
		form = FormAcc(instance=item)
		return render(request, 'item.html', {'form': form})

def delete(request, item_id):
	item = get_object_or_404(Acc, id=item_id)
	item.delete()
	return render(request, 'delete.html')
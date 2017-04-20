# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Acc

def index(request):
	accList = Acc.objects.all()
	context = {'accList': accList}
	return render(request, 'index.html', context)

def adiciona(request):
	if request.method == 'POST':
		form = Acc(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return render(request, 'salvo.html', {})
		return render(request, 'adiciona.html', {'form': form})
	else:
		form = Acc()
		return render(request, 'adiciona.html', {'form': form})
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Acc

def index(request):
	accList = Acc.objects
	context = {'accList': accList}
	return render(request, 'accs/index.html', context)
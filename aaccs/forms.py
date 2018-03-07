# -*- coding: utf-8 -*-
from django import forms
from aaccs.models import AACC
from django.forms import ModelForm

class FormAACC(ModelForm):
	class Meta:
		model = AACC
		fields = "__all__"

class FormSearch(forms.Form):
	busca = forms.CharField(max_length=200)

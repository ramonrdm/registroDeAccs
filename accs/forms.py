from django import forms
from models import Acc
from django.forms import ModelForm

class FormAcc(ModelForm):
	class Meta:
		model = Acc
		fields = "__all__"

class FormSearch(forms.Form):
	busca = forms.CharField(max_length=255)

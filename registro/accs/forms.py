from django import forms
from models import Acc
from django.forms import ModelForm

class FormAcc(ModelForm):
	class Meta:
		model = Acc
		fields = "__all__"
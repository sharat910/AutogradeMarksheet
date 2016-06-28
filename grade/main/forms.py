from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import *

class UploadForm(forms.Form):
    f = forms.FileField()
    n = forms.IntegerField(required=True,label='No. Of Students')
    t = forms.IntegerField(required=True,label='Total Marks')
    c = forms.CharField(required = True,label='Cell No. where marks begin')

class TestForm(forms.Form):
    bins = forms.IntegerField(required = False)
    binint = forms.CharField(label='Bin Intervals Between 0 and 100',required = False)
    freeze = forms.BooleanField(label='Freeze(Set final Bin Intervals)',required = False)

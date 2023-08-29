from django import forms 

class WordInputForm(forms.Form):
    word = forms.CharField(max_length=100)
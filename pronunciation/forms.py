from django import forms 

class WordInputForm(forms.Form):
    word = forms.CharField(max_length=100, required=False)

class GenerateTextForm(forms.Form):
    input = forms.CharField(max_length=1000, required=False, 
                            widget=forms.TextInput(attrs={'autocomplete': 'off'}))
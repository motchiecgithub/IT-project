from django import forms

class TranslationForm(forms.Form):
    english_text = forms.CharField(label='English Text', max_length=255)

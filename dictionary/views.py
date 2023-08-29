from django.shortcuts import render
from .forms import WordInputForm
import openai
import json 

OPENAI_API_KEY = "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"
openai.api_key = OPENAI_API_KEY

# Create your views here.
def translate(word):
    prompt = "Provide phonetic pronunciation for \"" + word + "\""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages = [
            {"role": "user", "content": prompt}
        ]
    )
    phonetic_pronunciation = response.choices[0]['message']['content']
    return phonetic_pronunciation
        


def dictionary(request): 
    if request.method == "POST":
        form = WordInputForm(request.POST)
        if form.is_valid():
            word = form.cleaned_data["word"]
            phonetic = translate(word)
            word_definition = "pass"
            return render(request, 'dictionary/index.html', 
                          {'form': form, 'phonetic_pronunciation': phonetic, 'word_definition': word_definition, 'word': word})
    else: 
        form = WordInputForm()
    return render(request, 'dictionary/index.html', {'form': form})
from django.shortcuts import render
from django.http import HttpResponse
from dotenv import load_dotenv
from .forms import WordInputForm
from .forms import GenerateTextForm
import os 
import openai
# Create your views here.


def translate(word):
    openai.api_key = OPENAI_API_KEY
    prompt = "Can you provide the Chinese pronunciation for \"" + word + "\""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages = [
            {"role": "system", "content": "You are a language expert."},
            {"role": "system", "content": "Please just return the answer, do not include anything else."},
            {"role": "user", "content": prompt}
        ]
    )
    phonetic_pronunciation = response.choices[0]['message']['content']
    return phonetic_pronunciation

def main_page(request):
    if request.method == "POST":
        generate_text_form = GenerateTextForm(request.POST)
        if generate_text_form.is_valid():
            input_text = generate_text_form.cleaned_data["input"]
            response = translate_word_logic(input_text)
            # response = generate_text_logic(input_text)
        else: 
            response = None
    else: 
        generate_text_form = GenerateTextForm()
        response = None
    return render(request, 'index.html', {
        'generate_text_form': generate_text_form,
        'response': response,
    })

def translate_word_logic(word):
    openai.api_key = OPENAI_API_KEY
    response = openai.ChatCompletion.create(
        model = "gpt-4",
        messages = [
            {"role": "system", "content": "You are a language translator"},
            {"role": "system", "content": "Translate all user input text to Chinese"},
            {"role": "user", "content": word}
        ]
    )
    return response.choices[0]['message']['content']
def generate_text_logic(input):
    openai.api_key = OPENAI_API_KEY
    response = openai.ChatCompletion.create(
        model = "gpt-4",
        messages = [
            {"role": "system", "content": "You are a text generator"},
            {"role": "system", "content": "Only return the text content"},
            {"role": "user", "content": input}
        ]    
        
    )
    return response.choices[0]['message']['content']



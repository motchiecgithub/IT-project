from django.http import HttpResponse
from django.template import loader
from .models import Member
from search import *
from django.shortcuts import render
from .forms import TranslationForm
from soundex import *
from flask import Flask, render_template, request, redirect, url_for, session, flash
from list_convert import *

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def translate_C(request):
  template = loader.get_template('translate_c.html')
  context = {}
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def translate(request):
  template = loader.get_template('translate.html')
  # show the returned value from phonetic_soundex and phonetic_metaphone 
  if request.method == 'POST':
    form = TranslationForm(request.POST)
    if form.is_valid():
            
            # testing the language----------
            language = "en_US"
            # testing the language----------
                        
            # format text by language type
            clean_text = form.cleaned_data['english_text']
            text = phonetic_translate_word(clean_text, language)

            # if the word is not in the dictionary
            if text == "Word Not found":
              context = {
                'text': text,
              }
              return render(request, 'translate.html', {'form': form, 'context': context})
            
            # if the word is in the dictionary
            if language == "en_US" or language == "en_UK":
              text_r = text[1]
            if language == "zh_hans":
              text_r = text[1:]

            letters = phonetic_translate_letter(text_r, list_convert(clean_text, language), language)
            #soundex = phonetic_soundex(english_text)
            #metaphone = phonetic_metaphone(english_text)
            
            context = {
              'text': text,
              #'soundex': soundex,
              #'metaphone': metaphone,
              'letters': letters,
            }
            return render(request, 'translate.html', {'form': form, 'context': context})
  else:
    form = TranslationForm()
  return render(request, 'translate.html', {'form': form})
            
def home(request):
  return render(request, 'home.html')

def process_word_link(request):
    word = request.POST['content']
    phonetic_text = phonetic_translate_word(word, "en_US")
    return HttpResponse(phonetic_text)




from django.http import HttpResponse
from django.template import loader
from .models import Member
from search import *
from django.shortcuts import render, redirect
from .forms import TranslationForm
from list_convert import *
from django.contrib import auth
from django.contrib.auth.models import User
from .gpt import gpt_definition, gpt_phonetic, gpt_translate, ask_gpt

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
    content = request.POST['content']
    content_lst = content.split("@")
    word = content_lst[0]
    language1 = content_lst[1]
    language2 = content_lst[2]
    translated_word = gpt_translate(word, language1, language2)
    definition = gpt_definition(word, language2)
    phonetic = gpt_phonetic(word, language2)
    similar = gpt_similar(word, language2)
    result = str(phonetic) + "@" + str(definition) + "@" + str(similar)
    return result
    
    

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            try:
                user = User.objects.create_user(username, email, password1)
                user.save()
                auth.login(request, user)
                return redirect('phonetic:translate_c')
            except:
                error_message = 'Error creating account'
                return render(request, 'register.html', {'error_message': error_message})
        else:
            error_message = 'Password dont match'
            return render(request, 'register.html', {'error_message': error_message})
    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('phonetic:translate_c')
        else:
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

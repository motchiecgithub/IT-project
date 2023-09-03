from django.http import HttpResponse
from django.template import loader
from .models import Member
from program import *

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

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def translate(request):
  template = loader.get_template('translate.html')
  # show the returned value from phonetic_soundex and phonetic_metaphone 
  if request.method == 'POST':
    form = TranslationForm(request.POST)
    if form.is_valid():
            english_text = form.cleaned_data['english_text']
            text = phonetic_translate(english_text, "en_US")
            soundex = phonetic_soundex(english_text)
            metaphone = phonetic_metaphone(english_text)
            context = {
              'text': text,
              'soundex': soundex,
              'metaphone': metaphone,
            }
            return render(request, 'translate.html', {'form': form, 'context': context})
  else:
    form = TranslationForm()
  return render(request, 'translate.html', {'form': form})

def index(request):
  return render(request, 'index.html')

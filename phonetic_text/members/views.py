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

def testing(request):
  template = loader.get_template('template.html')
  # show the returned value from phonetic_soundex and phonetic_metaphone
  context = {
    'soundex': phonetic_soundex('phonetic'),
    'metaphone': phonetic_metaphone('phonetic'),
  }
  return HttpResponse(template.render(context, request))
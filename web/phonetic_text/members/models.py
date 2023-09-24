from django.db import models

# define the user model with first and last name
class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    # add more information...

# define the translation model with english and phonetic text
class Translation(models.Model):
    english_text = models.CharField(max_length=255)
    phonetic_text = models.CharField(max_length=255)
    soundex = models.CharField(max_length=255)
    metaphone = models.CharField(max_length=255)

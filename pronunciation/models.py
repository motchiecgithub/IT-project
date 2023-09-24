from django.db import models

# Create your models here.

# store words and its definition 
class WordDefinitionModel(models.Model):
    word = models.CharField(max_length=100, unique=True)
    phonetic_pronunciation =  models.CharField(max_length=100)
    definition = models.TextField()
    def __str__(self):
        return self.word

# store auto generated text
class ParagraphModel(models.Model):
    text = models.TextField()
from django.db import models

# define the user model with first and last name
class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    # add more information...



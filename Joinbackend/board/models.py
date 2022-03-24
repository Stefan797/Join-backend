# from unicodedata import category
from cgitb import text
from django.conf import settings
from django.db import models

from datetime import date

# Create your models here.

class Tasks(models.Model):
    text = models.CharField(max_length=500) 
    # category = ArrayField(('', 'today', 'progress', 'done'))
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    created_at = models.DateField(default=date.today)
    color = models.CharField(max_length=500)
    discription = models.CharField(max_length=500)
# from unicodedata import category
from cgitb import text
from django.conf import settings
from django.db import models

from datetime import date

# Create your models here.

Category_one = "Todo"
Category_two = "Today"
Category_three = "In progress"
Category_four = "Done"

CATEGORY_CHOICES = (
    (Category_one, "Todo"),
    (Category_two, "Today"),
    (Category_three, "In progress"),
    (Category_four, "Done"),
)

class Tasks(models.Model):
    text = models.CharField(max_length=500) 
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    created_at = models.DateField(default=date.today)
    color = models.CharField(max_length=500)
    discription = models.CharField(max_length=500)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="Todo")
    
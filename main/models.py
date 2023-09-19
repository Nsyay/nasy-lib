from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=255, default="")
    author = models.CharField(max_length=255, default="")
    amount = models.IntegerField(default=0)
    genre = models.CharField(max_length=255, default="")
    description = models.TextField(default="")
    date_added = models.DateField(auto_now_add=True)
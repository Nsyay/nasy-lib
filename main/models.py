from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=255, default="Book Title")
    author = models.TextField(default="-")
    amount = models.IntegerField(default=0)
    genre = models.TextField(default="-")
    description = models.TextField(default="-")
    date_added = models.DateField(auto_now_add=True)
from django.db import models

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=255, default="Book Title")
    author = models.TextField(default="-")
    amount = models.IntegerField(default=0)
    genre = models.TextField(default="-")
    description = models.TextField(default="-")
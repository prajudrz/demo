from django.db import models

# Create your models here.
class Library(models.Model):
    book_name = models.CharField(max_length=50)
    book_details = models.TextField(max_length=100)
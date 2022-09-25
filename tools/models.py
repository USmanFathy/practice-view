from django.db import models

# Create your models here.

class Tool(models.Model):
    title = models.CharField(max_length=120)
    slug  = models.SlugField() 
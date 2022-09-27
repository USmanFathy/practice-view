from django.db import models
from django.conf import settings 

# Create your models here.

User = settings.AUTH_USER_MODEL

class Tool(models.Model):
    user  = models.ForeignKey(User , blank=True , null=True , on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    slug  = models.SlugField(unique=True) 

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return f"/list/{self.slug}/"

    def get_edit_url(self):
        return f"/list/{self.slug}/"

    def get_delete_url(self):
        return f"/list/{self.slug}/delete/"
    





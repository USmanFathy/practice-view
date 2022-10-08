from django.db import models
from django.conf import settings 










class Tool(models.Model):
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










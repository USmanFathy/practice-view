from django.db import models
from django.conf import Settings
from django.db.models.signals import post_save
# Create your models here.

User = Settings.AUTH_USER_MODEL


class Account(models.Model):
    user  = models.OneToOneField(User)
    city  = models.CharField(max_length=120 , null=True , blank=True)


    def __str__(self) -> str:
        return self.user.username


def post_save_user_model_receiver(sender , instance , created , *args, **kwargs):
    if created :
        try:
            Account.objects.create(user= instance)
        except:
            pass

post_save.connect(post_save_user_model_receiver , sender= User)

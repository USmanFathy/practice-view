from django.db import models
from django.conf import Settings
from django.db.models.signals import post_save
from django.core.validators import RegexValidator
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        """
        Creates and saves a User with the given email, username and password.
    
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username, # user name can't be self just what we made 
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        """
        Creates and saves a superuser with the given email, username and password.
        """
        user = self.create_user(
            email,
            username, # put here what aguments come
            password=password,
            
        )
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user


USERNAME_REGEX = '^[a-zA-Z0-9.@+-]*s'


class MyUser(AbstractBaseUser):
    username = models.CharField(
                        max_length = 225 ,
                        validators = [RegexValidator(
                            regex=USERNAME_REGEX,
                            message="Username must be Alphnumeric or contain any of the followings: '. @ + - '",
                            code = "invalid_username"
                        )],
                        unique = True
                                )
    email    = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    # @property
    # def is_staff(self):
    #     "Is the user a member of staff?"
    #     # Simplest possible answer: All admins are staff
    #     return self.is_admin









# User = Settings.AUTH_USER_MODEL


# class Account(models.Model):
#     user  = models.OneToOneField(User)
#     city  = models.CharField(max_length=120 , null=True , blank=True)


#     def __str__(self) -> str:
#         return self.user.username


# def post_save_user_model_receiver(sender , instance , created , *args, **kwargs):
#     if created :
#         try:
#             Account.objects.create(user= instance)
#         except:
#             pass

# post_save.connect(post_save_user_model_receiver , sender= User)

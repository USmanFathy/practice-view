from django import forms
from .models import MyUser , USERNAME_REGEX
from django.core.validators import RegexValidator
# from django.contrib.auth import authenticate
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.db.models import Q

class UserLoginForm(forms.Form):
    query = forms.CharField(label='Username / Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    def clean(self,*args, **kwargs):
        query = self.cleaned_data.get('query')
        password = self.cleaned_data.get('password')

        # user_qs1 = MyUser.objects.filter(username__iexact=query)
        # user_qs2 = MyUser.objects.filter(username__iexact=query)
        # user_qs_final = (user_qs1 | user_qs2).distinct() this 3 line hit model more than one time so it render error
        user_qs_final = MyUser.objects.filter(
            Q(username__iexact=query)|
            Q(email__iexact=query)
        )
        if not user_qs_final.exists() and user_qs_final.count() != 1 :
            raise forms.ValidationError("You have add Invalid Username or Password ! ")

        user_object =user_qs_final.first()

        if not user_object.check_password(password):
            raise forms.ValidationError("You have add Invalid Username or Password ! ")

        # if not user_object.is_active():
        #     raise forms.ValidationError("You have add Inactive Account ! ")

        self.cleaned_data['user_object']=user_object
        return super(UserLoginForm ,self).clean(*args, **kwargs)



class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('username','email')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_active = False
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('email', 'password', 'username', 'is_active','is_staff', 'is_admin')



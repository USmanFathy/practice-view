from django import forms
from .models import MyUser , USERNAME_REGEX
from django.core.validators import RegexValidator
# from django.contrib.auth import authenticate
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

class UserLoginForm(forms.Form):
    username = forms.CharField(label='Username' , validators=[RegexValidator(
                            regex=USERNAME_REGEX,
                            message="Username must be Alphnumeric or contain any of the followings: '. @ + - '",
                            code = "invalid_username"
                        )]
                        
                        )
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    def clean(self,*args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user_object = MyUser.objects.filter(username=username).first()

        if not user_object:
            raise forms.ValidationError("You have add Invalid Username or Password ! ")
        else :
            if not user_object.check_password(password):
                raise forms.ValidationError("You have add Invalid Username or Password ! ")
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



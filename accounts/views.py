from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView ,View ,UpdateView
from django.contrib.auth import logout , login
from.models import MyUser
from .forms import UserCreationForm , UserLoginForm ,UserChangeForm



class CreatNewUser(CreateView):
    form_class= UserCreationForm
    template_name: str = 'accounts/register.html'
    success_url='/login'

    def form_valid(self , form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super().form_valid(form)
    
    def form_invalid(self , form):
        return super().form_invalid(form)




    # def get_success_url(self) -> str:
    #     return HttpResponseRedirect('/login')

def user_login(request ,*args, **kwargs):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        user_obj   = form.cleaned_data.get('user_object')
        # userobject = MyUser.objects.get(username__iexact = username_)
        login(request , user_obj)
        return HttpResponseRedirect ("/list")
    return render(request , 'accounts/login.html', {'form':form})



def user_log_out(request):
    logout(request)

    return HttpResponseRedirect('/login')
from django.shortcuts import render
from django.views.generic import CreateView
from .forms import UserCreationForm



class CreatNewUser(CreateView):
    form_class= UserCreationForm
    template_name: str = 'accounts/register.html'
    success_url='/list'

    def form_valid(self , form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super().form_valid(form)
    
    def form_invalid(self , form):
        return super().form_invalid(form)


from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
        TemplateView,
        ListView ,
        DetailView,
        View,
        RedirectView,
        CreateView
        )
from django.contrib.auth.decorators import login_required
from django.views.generic.list import MultipleObjectMixin
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.utils.decorators import method_decorator
from .forms import ToolForm
from .mixins import ToolTemplateMixin
from.models import Tool
# Create your views here.



class Team(TemplateView):
    template_name = 'tools/about.html'

# class Modelmixin():
#     model = None

#     def get_template(self):
#         if self.model is None:
#             raise Exception("Set your model please !")
        # model_name= self.model._meta.model_name
        # app_label= self.model._meta.app_label
        # template = f"{app_label}/{model_name}_list.html"
#         return template


#     def get_queryset(self):
#         return self.model.objects.all()
    

#     def get_context_data(self):
#         context={
#             'object_list':self.get_queryset()
#         }
#         return context
    











class ShowTooLS( MultipleObjectMixin,View):
    model = Tool
    title = 'Tools'
    

    def get(self , request ,*args , **kwargs):
        self.object_list =self.get_queryset()
        model_name= self.model._meta.model_name
        app_label= self.model._meta.app_label
        template = f"{app_label}/{model_name}_list.html"
        context =self.get_context_data()
        return render(request,template,context)






class ShowTooLSog(ToolTemplateMixin,ListView):
    model = Tool
    title = 'Tools'






class Showitem(LoginRequiredMixin,DetailView):
    model = Tool


    # def get_object(self):

    #     url_id = self.kwargs.get('id')
    #     qs = self.get_queryset().filter(id=url_id)
    #     return qs.get() 
    # @method_decorator(login_required)
    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(request, *args, **kwargs)
    




class CreatNewTool(LoginRequiredMixin,CreateView):
    form_class= ToolForm
    template_name: str = 'tools/forms.html'
    # success_url='/list'

    def form_valid(self , form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super().form_valid(form)
    def form_invalid(self , form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super().form_invalid(form)
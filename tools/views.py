
from django.views.generic import TemplateView,ListView ,DetailView,View
from django.views.generic.list import MultipleObjectMixin
from django.shortcuts import render
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






class Showitem(ToolTemplateMixin,DetailView):
    model = Tool
    template_name: str = "tools/detail.html"

    def get_object(self):

        url_id = self.kwargs.get('id')
        qs = self.get_queryset().filter(id=url_id)
        return qs.get() 







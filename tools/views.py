
from django.views.generic import TemplateView,ListView ,DetailView
from.models import Tool
# Create your views here.


class Team(TemplateView):
    template_name = 'tools/about.html'


class ShowTooLS(ListView):
    model = Tool
    template_name = "tools/show.html"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        return context



class Showitem(DetailView):
    model = Tool
    template_name = "tools/detail.html"
    



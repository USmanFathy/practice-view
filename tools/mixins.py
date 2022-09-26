class ToolTemplateMixin(object):
    title = None
    template_name = "tools/tool_list.html"
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['title'] = self.get_title()
        return context

    def get_title(self):
        return self.title
    pass

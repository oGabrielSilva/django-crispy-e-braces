from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'paginas/base.html'


class SobreView(TemplateView):
    template_name = 'paginas/sobre.html'

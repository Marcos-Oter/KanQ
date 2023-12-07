from django.views.generic import TemplateView

# Create your views here.

class homeIndex(TemplateView):
    template_name="main-index.html"
from django.views.generic import TemplateView

class TestPage(TemplateView):
    template_name = 'firstapp/test.html'

class ThanksPage(TemplateView):
    template_name = 'firstapp/thanks.html'

class HomePage(TemplateView):
    template_name = 'firstapp/index.html'

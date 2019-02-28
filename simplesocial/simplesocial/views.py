from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse


class TestPage(TemplateView):
    template_name = 'test.html'


class ThanksPage(TemplateView):
    template_name = 'thanks.html'


class HomePage(TemplateView):
    template_name = "index.html"

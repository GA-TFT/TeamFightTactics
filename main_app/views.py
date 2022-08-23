from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'

class Champions(TemplateView):
    template_name = 'champions.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["champions"] = Champions
        return context

class Augments(TemplateView):
    template_name = 'augments.html'

class TraitsList(TemplateView):
    template_name = 'traits.html'

# class Champions(View):
#     def get(self, request):
#         return HttpResponse("Champions Page")
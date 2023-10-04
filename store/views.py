from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class HomeTemplateView(TemplateView):
    template_name = 'store/home.html'


def about_us(request):
    return render(request, 'info/about_us.html')
def terms(request):
    return render(request, 'info/terms.html')

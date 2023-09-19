from django.views.generic import TemplateView


# Create your views here.

class HomeTemplateView(TemplateView):
    template_name = 'store/home.html'
    # obj = Carousels.objects.all()
    # context = {'carusel': obj}

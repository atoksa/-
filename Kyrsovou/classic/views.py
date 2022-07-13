
from django.shortcuts import render
from .models import CLASSIC
from django.views.generic import DetailView

def classic(request):
    books = CLASSIC.objects.order_by('-data')

    return render(request, 'classic.html', {"books": books})


class detail(DetailView):
    model = CLASSIC
    template_name = 'classic_2.html'
    context_object_name = 'clas'

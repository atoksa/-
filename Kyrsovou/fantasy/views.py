from django.shortcuts import render
from .models import FANTASY
from django.views.generic import DetailView

def fantasy(request):
    books = FANTASY.objects.order_by('-data')

    return render(request, 'fantasy.html', {"books": books})


class detail(DetailView):
    model = FANTASY
    template_name = 'fantasy_2.html'
    context_object_name = 'fant'

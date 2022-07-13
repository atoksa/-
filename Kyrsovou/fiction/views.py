from django.shortcuts import render
from .models import FICTION
from django.views.generic import DetailView

def fiction(request):
    books = FICTION.objects.order_by('-data')

    return render(request, 'fiction.html', {"books": books})


class detail(DetailView):
    model = FICTION
    template_name = 'fiction_2.html'
    context_object_name = 'fict'
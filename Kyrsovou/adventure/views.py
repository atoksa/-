from django.shortcuts import render
from .models import ADVENTURE
from django.views.generic import DetailView


def adventure(request):
    book = ADVENTURE.objects.order_by('-data')

    return render(request, 'adventure.html', {"book": book})


class detail(DetailView):
    model = ADVENTURE
    template_name = 'adventure_2.html'
    context_object_name = 'adv'




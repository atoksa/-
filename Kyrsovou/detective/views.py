from django.shortcuts import render
from .models import DETECTIVE
from django.views.generic import DetailView

def detective(request):
    books = DETECTIVE.objects.order_by('-data')

    return render(request, 'detective.html', {"books": books})


class detail(DetailView):
    model = DETECTIVE
    template_name = 'detective_2.html'
    context_object_name = 'detec'
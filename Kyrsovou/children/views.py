from django.shortcuts import render
from .models import CHILDREN
from django.views.generic import DetailView

def child(request):
    books = CHILDREN.objects.order_by('-data')

    return render(request, 'children.html', {"books": books})


class detail(DetailView):
    model = CHILDREN
    template_name = 'children_2.html'
    context_object_name = 'det'


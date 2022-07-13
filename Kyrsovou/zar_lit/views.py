from django.shortcuts import render
from .models import ZAR_LIT, Comment
from django.views.generic import DetailView
from .forms import CommentFrom


def zar_lit(request):
    books = ZAR_LIT.objects.order_by('-data')

    return render(request, 'zar_lit.html', {"books": books})


class detail(DetailView):
    model = ZAR_LIT
    template_name = 'zar_lit_2.html'
    context_object_name = 'zar_lists'


def blog_detail(request):
    post = Comment.objects.get
    forms = CommentFrom()
    if request.method == 'POST':
        forms = CommentFrom(request.POST)
        if forms.is_valid():
            comment = Comment(
                author=forms.cleaned_data["author"],
                body=forms.cleaned_data["body"],
                post=post
            )
            comment.save()

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": forms,
    }
    return render(request, 'zar_lit_2.html', context)

# def create(request):
#     form = CommentFrom()
#     data = {'form': form}
#
#     return render(request, 'zar_lit_2.html', data)

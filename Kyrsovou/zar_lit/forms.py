from django import forms
from .models import Comment, ZAR_LIT
from django.forms import ModelForm


class CommentFrom(forms.Form):
    author = forms.CharField(max_length=60,
                             widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Ваше имя"}))
    body = forms.CharField(widget=forms.Textarea(attrs={"class": "from-contol", "placeholder": "Оставьте комментарий"}))


# class CommentFrom(ModelForm):
#     class Meta:
#         model = ZAR_LIT
#         fields = ['title', 'author', 'briefly']
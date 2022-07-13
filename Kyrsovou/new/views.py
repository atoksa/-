from django.shortcuts import render


def nachalo(request):
    return render(request,'new/nachalo.html')


def second(request):
    return render(request,'new/second.html')

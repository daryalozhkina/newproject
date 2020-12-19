from django.shortcuts import render

from myapp.models import Category


def index(request):
    return render(request, 'myapp/index.html')


def staffes(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'staffes': 'сотрудники'
    }
    return render(request, 'myapp/staffes.html', context)

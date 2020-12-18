from django.shortcuts import render

from myapp.models import Category, Groups


def index(request):
    return render(request, 'myapp/index.html')


def students(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'students': 'студенты'
    }
    return render(request, 'myapp/students.html', context)


def groups(request):
    return render(request, 'myapp/groups.html')


def students_page(request, pk):
    group = Groups.objects.filter(category_id=pk)
    context = {
        'group': group,
        'students_page': 'страница студентов'
    }
    return render(request, 'myapp/students_page.html', context)

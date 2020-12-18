from django.shortcuts import render

def index(request):
    return render(request, 'myapp/index.html')


def students(request):
    pass
# Create your views here.

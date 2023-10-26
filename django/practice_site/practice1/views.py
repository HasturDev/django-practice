from django.shortcuts import render
from .models import MyModel
# Create your views here.

def home(request):
    context = {'data' : MyModel.objects.all()}
    return render(request, 'home.html', context)

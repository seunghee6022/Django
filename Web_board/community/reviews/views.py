from django.shortcuts import render
from .models import Review

# Create your views here.
def index(request):
    return render(request,'reviews/index.html')
    
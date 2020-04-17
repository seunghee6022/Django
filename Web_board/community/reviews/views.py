from django.shortcuts import render, redirect
from .models import Review

# Create your views here.
def index(request):
    reviews = Review.objects.all()
    context = {
        'reviews' : reviews
    }
    return render(request,'reviews/index.html',context)

def new(request):
    return render(request, 'reviews/new.html')


def create(request):
    review = Review()
    review.title = request.GET.get('title')
    review.content = request.GET.get('content')
    review.rank = request.GET.get('rank')
    review.save()
    return redirect('reviews:index')


        

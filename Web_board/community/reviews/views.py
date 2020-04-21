from django.shortcuts import render, redirect,get_object_or_404
from .models import Review
from .forms import ReviewForm
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    reviews = Review.objects.all()
    context = {
        'reviews' : reviews
    }
    return render(request,'reviews/index.html',context)

def create(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            return redirect('reviews:index')
    else :
        form = ReviewForm()
    context = {
        'form' : form
    }
    return render(request, 'reviews/form.html',context)


def detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    context = {
        'review' : review
    }
    return render(request, 'reviews/detail.html', context)

        

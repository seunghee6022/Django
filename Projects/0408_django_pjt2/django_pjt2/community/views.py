from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_POST
from .models import Review
from .forms import ReviewForm

# Create your views here.
def index(request):
    articles = Review.objects.order_by('-rank')
    context = {
        'articles': articles
    }
    return render(request,'community/review_list.html',context)

def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:index')

    else :
        form = ReviewForm()
    context = {
        'form' : form
    }
    return render(request, 'community/form.html', context)
    
def detail(request, pk):
    article = get_object_or_404(Review, pk=pk)
    context = {
        'article': article
    }
    return render(request, 'community/review_detail.html',context)

def update(request,pk):
    article = get_object_or_404(Review,pk=pk)

    if request.method =='POST':
        form = ReviewForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else :
        form = ReviewForm(instance = article)

    context = {
        'article' : article,
        'form': form
    }
    return render(request, 'community/form.html', context)

@require_POST
def delete(request,pk):
    article = get_object_or_404(Review, pk=pk)
    article.delete()
    return redirect('articles:index')

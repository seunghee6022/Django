from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from django.http  import JsonResponse



# Create your views here.
def movie_list(request):
    movies = Movie.objects.all()

    paginator = Paginator(movies, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'movies': movies,
        'page_obj': page_obj,
    }
    return render(request, 'movies/movie_list.html', context)

def overview(request,movies_pk):
    movie = get_object_or_404(Movie, pk=movies_pk)
    context = {
        'movie': movie,   
    }
    return render(request, 'movies/overview.html', context)




def like(request, movies_pk):
    user = request.user 
    movie = get_object_or_404(Movie, pk=movies_pk)
    
    if user.is_authenticated :
        if movie.like_users.filter(pk=user.pk).exists():
            movie.like_users.remove(user)
            liked = False # 좋아요 눌렀는지 안눌렀는지 확인로직
        else:
            movie.like_users.add(user)
            liked = True

    else :
        return redirect('accounts:login')
    context = {
        'liked': liked,
        'count' : movie.like_users.count(),
    }
    return JsonResponse(context)


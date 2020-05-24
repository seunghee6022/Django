from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm
from .models import User
from movies.models import Genre, Movie
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.http import require_POST
# Create your views here.

def signup(request):
    if request.user.is_authenticated:
        return redirect('movies:movie_list')

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('movies:movie_list')
    else :
        form = CustomUserCreationForm()

    context = {
        'form':form,
    }
    return render(request, 'accounts/signup.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('movies:movie_list')
    
    if request.method =="POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'movies:movie_list')

    else :
        form = AuthenticationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/login.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('movies:movie_list')

@login_required
def recommendation(request):
    genres = Genre.objects.all()
    User = get_user_model()    
    user = get_object_or_404(User, pk=request.user.pk)
    good_movies = Movie.objects.order_by('-vote_average')
    movies = user.like_movies.all()
 
    genres_dict = {}
    for genre in genres:
        genres_dict[genre.name] = 0
  
    for movie in movies:
        for genre in movie.genres.all():           
            genres_dict[genre.name]+=1
      
    sorted_genres_dict = sorted(genres_dict.items(), key=lambda kv: kv[1], reverse=True)
    genres_dict= dict(sorted_genres_dict)
    keys = []
    for key in genres_dict.keys():
        keys.append(key)
   
    recommand = []
    for good_movie in good_movies:
        
        check = [0,0,0]
        for genre in good_movie.genres.all():
            print(type(genre))
            if genre.name == keys[0]:
                check[0] = 1
            elif genre.name == keys[1]:
                check[1] = 1
            elif genre.name == keys[2]:
                check[2] = 1
        if 0 not in check:
            recommand.append(good_movie)



    context = {
        '1st_genre': keys[0],
        '2nd_genre': keys[1],
        '3rd_genre': keys[2],
        'good_movies':good_movies,
        'recommand': recommand[:10],
        'movies':movies,
    }

    
    return render(request, 'accounts/recommendation.html', context)
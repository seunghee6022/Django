# Django Project5

### 구현과정

1. 명세대로 genre와 movie model을 마이그레이션한 후 `python manage.py loaddata moviedata.json`을 이용해 데이터를 로드합니다.

2. 로그인기능을 만들어 인증된 사용자에 한해 영화 좋아요를 할 수 있게 합니다.

3. 영화 조회는 카드형식으로 보여주었고 페이지네이션으로 10개씩 보여주게 했습니다.

4. 각 영화는 줄거리를 따로 상세페이지에서 볼 수 있게 하였습니다.

5. 영화 추천은 사용자가 좋아요한 영화 데이터를 기반으로 좋아요 누른 영화들의 장르를 카운트하여 가장 높은 카운트가 나온 3순위의 장르와 높은 투표평점을 기준으로 영화를 추천하였습니다.

   ```python
   @login_required
   def recommendation(request):
       
       User = get_user_model()    
       user = get_object_or_404(User, pk=request.user.pk)
       
       # 높은 평점순으로 정렬된 영화
       good_movies = Movie.objects.order_by('-vote_average')
       
       # 사용자가 좋아요 누른 영화들
       movies = user.like_movies.all()
    	
       # 카운팅을 위해 장르를 가져와서 딕셔너리로 만듭니다.
       genres = Genre.objects.all()
       genres_dict = {}
       for genre in genres:
           genres_dict[genre.name] = 0
     	#사용자가 좋아요한 영화에서 장르 카운트
       for movie in movies:
           for genre in movie.genres.all():           
               genres_dict[genre.name]+=1
       # 내림차순 정렬
       sorted_genres_dict = sorted(genres_dict.items(), key=lambda kv: kv[1], reverse=True)
       genres_dict= dict(sorted_genres_dict)
       
       #장르명 쉽게 빼오기 위한 key리스트
       keys = []
       for key in genres_dict.keys():
           keys.append(key)
      
   	#높은 평점 영화부터 시작해서 사용자가 가장 많이 좋아한 장르 3위를 모두 만족하면 영화 추천대상에 넣습니다.
       recommand = []
       for good_movie in good_movies:
           
           check = [0,0,0]
           for genre in good_movie.genres.all():
               if genre.name == keys[0]:
                   check[0] = 1
               elif genre.name == keys[1]:
                   check[1] = 1
               elif genre.name == keys[2]:
                   check[2] = 1
           if 0 not in check:
               recommand.append(good_movie)
       print(recommand)
   
   
       context = {
           '1st_genre': keys[0],
           '2nd_genre': keys[1],
           '3rd_genre': keys[2],
           'good_movies':good_movies,
           'recommand': recommand[:10],
           'movies':movies,
       }
   
       
       return render(request, 'accounts/recommendation.html', context)
   ```



### 페어프로그래밍에서 느낀점

1. 서로가 무엇을 할 수 있는지 정하는 것이 생각보다 어렵다.
2. 각자가 하기로 한 것을 하는것이 생각보다 어렵다.
3. 결국 모든 팀원이 전반적으로 좋은 지식을 가지고 있는 것이 많은 도움이 된다.



### 어려웠던점

1. 영화추천하는 과정에서 object타입인지 아닌지에 따라 genres에 접근 유무가 달라져서 query문을 사용하는데 있어 많은 시행착오를 겪었습니다.
2. html에서는 확실히 리스트나 딕셔너리 등 원하는 값을 빼오기에 많은 한계가 있어 파이썬을 사용했습니다.
3. 추천과정에서 사용자가 좋아요한 장르를 filter로 간편하게 거르고 싶었지만 genres자체 내에서 또 <class 'movies.models.Genre'>라는 클래스 안에 있어서 filter로 속성을 접근하는게 어려웠습니다.
4. 그래서 결국 파이썬의 기능을 많이 이용하여 추천알고리즘을 구현했는데 정말 많은 시도를 하였고 실패하며 결국 파이썬 views.py에서 구현하는 것이 제일 쉽다는 것을 깨닫기까지 시간이 많이 소요되었습니다.
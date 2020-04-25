# 0414 세션/쿠키 Workshop

### views.py

```python
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
def index(request):
    User = get_user_model()
    members = User.objects.all()
    context = {
        'User': User,
        'members' : members
    }
    return render(request,'accounts/index.html',context)
 

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #회원 가입하자마자 자동 로그인까지 가능
            auth_login(request,user)
            return redirect('accounts:index')

    else :
        form = UserCreationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request,form.get_user())
            return redirect('accounts:index')
    else :
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/signup.html', context)

def logout(request):
    auth_logout(request)
    return redirect('accounts:index')
```

---

### 결과 사진

* 로그인 전

![](C:\Users\tgb03\Desktop\online-lecture\0414\workshop\로그인전.PNG)

* 회원가입

![](C:\Users\tgb03\Desktop\online-lecture\0414\workshop\회원가입.PNG)

* 로그인

![](C:\Users\tgb03\Desktop\online-lecture\0414\workshop\로그인.PNG)

* 로그인 후

![](C:\Users\tgb03\Desktop\online-lecture\0414\workshop\로그인 후.PNG)
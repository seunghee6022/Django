from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request,'index.html')

def lotto(request):
    import random
    pick = random.sample(range(1,46),6)
    context= { 'pick' : pick}
    return render(request, 'lotto.html', context)

def iam(request):
    return render(request, 'iam.html')

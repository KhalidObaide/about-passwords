from django.shortcuts import render
from django.http import HttpResponse
from .models import User


# Create your views here.
def index(request):
    if request.method != 'POST':
        context = {}
        return render(request, 'index.html', context)

    else:
        try:
            username = request.POST['username']
            password = request.POST['password']
        except:
            return HttpResponse('Some Problem cannot get the fields ')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return HttpResponse('No user called '+ username)

        if password == user.password:
            return HttpResponse('YAYA Got hacked ')
        else:
            return HttpResponse('Wrong password Bitch')
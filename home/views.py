from django.shortcuts import render
from django.http import HttpResponse


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

        return HttpResponse('YAYYAY Logged in ')
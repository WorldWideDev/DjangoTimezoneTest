from django.shortcuts import render, redirect, HttpResponse, reverse
from django.utils import timezone
from django.contrib import messages
import pytz
from .models import User
# Create your views here.
def timezone(request):
    request.session['django_timezone'] = request.POST['tz']
    print(request.POST['tz'])
    return HttpResponse(f"Timezone successfull set to {request.POST['tz']}")

def index(request):
    
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if not User.objects.authenticate(email, password):
            messages.error(request, 'Invalid Credentials')
            return redirect('home:index')
        user = User.objects.get(email=email)
        request.session['user_id'] = user.id
        return redirect('posts:index')
    return redirect('home:index')

def logout(request):
    del request.session['user_id']
    return redirect('/')

def create(request):
    if request.method == 'POST':
        errors = User.objects.validate(request.POST)
        if errors:
            for e in errors.values():
                messages.error(request, e)
            return redirect('home:index')
        else:
            user = User.objects.register(request.POST)
            request.session['user_id'] = user.id
            return redirect('posts:index')
    return redirect('/')


from django.shortcuts import render, redirect
from home.models import User
from .models import Post
# Create your views here.
def index(request):
    context = {
        'posts': Post.objects.order_by('-created_at'),
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'posts.html', context)

def create(request):
    user_in_session = User.objects.get(id=request.session['user_id'])
    Post.objects.create(content=request.POST['content'], author=user_in_session)
    return redirect('posts:index')
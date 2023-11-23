from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from posts.models import Posts


@login_required(login_url="login-url")
def home(request):
    all_post = Posts.objects.all()
    contex = {"posts": all_post}
    return render(request, 'index.html', contex)


@login_required(login_url="login-url")
def post(request):
    return render(request, 'post.html')

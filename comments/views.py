from django.shortcuts import render, redirect
from .models import Comments
from django.contrib import messages


# Create your views here.
def send_comment(request):
    if request.method == "POST":
        comment = request.POST.get('comment')
        comment_user = request.POST.get('comment_user')
        post_id = request.POST.get('post_id')

        store = Comments(comment=comment, comment_user=comment_user, post_id=post_id)
        store.save()
        messages.success(request, 'Comment posted successfully')
        return redirect('my-posts-url')

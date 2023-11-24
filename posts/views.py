from django.shortcuts import render, redirect
from .forms import PostsForm
from django.contrib import messages
from .models import Posts


# Create your views here.
def add_post(request):
    if request.method == "POST":
        form = PostsForm(request.POST, request.FILES)
        if form.is_valid():

            obj = form.save(commit=False)
            obj.post_user = request.user.username
            obj.save()
            messages.success(request, 'Post saved successfully')
            return redirect('add-post-url')
        else:
            messages.error(request, "Post saving failed ")
            return redirect('add-post-url')
    else:
        form = PostsForm()

    return render(request, 'posts/add-post.html', {'form': form})


def my_posts(request):
    myposts = Posts.objects.all()
    contex = {"posts": myposts}
    return render(request, 'posts/my-posts.html', contex)


def delete(request, id):
    item = Posts.objects.get(id=id)
    item.delete()
    messages.success(request, "Post deleted successfully")
    return redirect('my-posts-url')


def edit_post(request, id):
    item = Posts.objects.get(id=id)
    content = {"posts": item}
    if request.method == "POST":
        title = request.POST.get('title')
        body = request.POST.get('body')
        category = request.POST.get('category')
        post_user = request.POST.get('post_user')
        image = request.FILES.get('image')
        item.title = title
        item.body = body
        item.category = category
        item.post_user = post_user
        item.image = image
        item.save()
        messages.success(request, "Post updated successfully")
        return redirect("home-url")

    return render(request, 'posts/edit-post.html', content)


def show(request, id):
    post = Posts.objects.get(id=id)
    return render(request, 'blog-post.html', {'post': post})

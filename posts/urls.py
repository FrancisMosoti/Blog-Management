from django.urls import path
from . import views as my_views

urlpatterns = [
    path('add-post/', my_views.add_post, name="add-post-url"),
    path('my-post/', my_views.my_posts, name="my-posts-url"),
    path('show-post/<id>', my_views.show, name="show"),
    path('edit-post/<id>/', my_views.edit_post, name="edit-post"),
    path('delete/<id>', my_views.delete, name='delete'),


]

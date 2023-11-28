from django.urls import path
from . import views as my_views

urlpatterns = [
    path('comment/', my_views.send_comment, name="send-comment-url"),
]

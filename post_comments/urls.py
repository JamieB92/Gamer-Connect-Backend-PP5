from django.urls import path
from post_comments import views

urlpatterns = [
    path('post_comments/', views.PostCommentList.as_view()),
]
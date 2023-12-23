from django.urls import path
from .views import (
    GetAllPosts,
    CreatePost,
    GetPostAndComments,
    CreateComment,
)

name = 'post'
urlpatterns = [
    path('', GetAllPosts.as_view(), name='get_all_posts'),
    path('create/', CreatePost.as_view(), name='post_create'),
    path('<int:post_id>/', GetPostAndComments.as_view(), name='get_post_and_comments'),
    path('<int:post_id>/comments/create/', CreateComment.as_view(), name='create_comment'),
]

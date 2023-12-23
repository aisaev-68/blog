from django.urls import path
from django.views.generic import TemplateView



name = 'frontend'
urlpatterns = [
    path('', TemplateView.as_view(template_name="frontend/posts.html"), name='posts'),
    path('posts/<int:pk>/', TemplateView.as_view(template_name="frontend/post_detail.html"), name='post-detail'),
    path('post_create/', TemplateView.as_view(template_name="frontend/post_create.html"), name='create_post'),
    path('login/', TemplateView.as_view(template_name="frontend/login.html"), name='login'),
    path('register/', TemplateView.as_view(template_name="frontend/register.html"), name='register'),
    path('logout/', TemplateView.as_view(), name='logout'),
]

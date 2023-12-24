from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema

from .models import Post, Comment
from .serializers import (
    PostSerializer,
    CommentSerializer,
    CommentCreateSerializer,
    PostCreateSerializer,
)


class CreatePost(APIView):
    """
    API создания постов.
    """
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(request_body=PostCreateSerializer)
    def post(self, request):
        serializer = PostCreateSerializer(data={**request.data, 'author': request.user.id})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetAllPosts(APIView):
    """
    API получения постов.
    """

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class GetPostAndComments(APIView):
    """
    API получения поста и комментариев к нему.
    """

    def get(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        comments = Comment.objects.filter(post=post)
        post_serializer = PostSerializer(post)
        comment_serializer = CommentSerializer(comments, many=True)

        data = {
            "post": post_serializer.data,
            "comments": comment_serializer.data
        }
        return Response(data)


class CreateComment(APIView):
    """
    API создания комментария.
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=CommentSerializer)
    def post(self, request, post_id):

        serializer = CommentCreateSerializer(data={**request.data, 'post': post_id, 'author': request.user.id})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

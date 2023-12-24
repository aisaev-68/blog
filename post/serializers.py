from rest_framework import serializers
from django.urls import reverse

from .models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Сериализатор комментариев.
    """
    author = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'text', 'created_at']

    def get_author(self, obj) -> str:
        return f"{obj.author.first_name} {obj.author.last_name}"


class PostSerializer(serializers.ModelSerializer):
    """
    Сериализатор постов с комментариями.
    """
    comments = CommentSerializer(many=True, read_only=True)
    author = serializers.SerializerMethodField()
    href = serializers.SerializerMethodField()
    short_title = serializers.SerializerMethodField()
    short_content = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'href', 'title', 'short_title', 'content', 'short_content', 'created_at', 'author', 'comments']

    def get_author(self, obj) -> str:
        return f"{obj.author.first_name} {obj.author.last_name}"

    def get_short_title(self, obj) -> str:
        return f'{obj.title[:50]}...'

    def get_short_content(self, obj) -> str:
        return f'{obj.content[:200]}...'

    def get_href(self, obj) -> str:
        """
        Получение ссылки на пост.
        :return: ссылка
        """
        return reverse('post-detail', args=[obj.pk])


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

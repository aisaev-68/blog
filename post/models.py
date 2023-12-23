from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Модель постов.
    """
    title = models.CharField(
        max_length=100,
        verbose_name='title',
    )
    content = models.TextField(
        verbose_name='content',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='date',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='author',
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ["title", "content"]

    def href(self):
        """
        Получение ссылки жанров.
        :return: ссылка
        """
        return reverse('post-detail', args=[str(self.pk)])


class Comment(models.Model):
    """
    Модель комментариев.
    """
    post = models.ForeignKey(
        Post,
        related_name='comments',
        on_delete=models.CASCADE,
        verbose_name='post',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='author',
    )
    text = models.TextField(
        verbose_name='comment',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='date',
    )

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ["text", "author"]
import random
from mimesis import Text
from mimesis.locales import Locale
from django.contrib.auth.models import User
from django.core.management import BaseCommand

from post.models import Post


class Command(BaseCommand):
    """
    Creates products
    """

    def handle(self, *args, **options):
        self.stdout.write("Create posts")
        user = User.objects.filter(username='admin').first()

        for _ in range(20):
            text = Text(locale=Locale.RU)

            Post.objects.create(
                title=text.title(),
                content=text.text(),
                author=user,
            )
        self.stdout.write(self.style.SUCCESS("Posts created"))
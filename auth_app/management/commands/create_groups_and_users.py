from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, User
from django.contrib.auth.models import Permission
from mimesis import Person
from mimesis.locales import Locale
from mimesis.enums import Gender

from post.models import Post, Comment


class Command(BaseCommand):
    help = 'Creates read only default permission groups for users'

    def handle(self, *args, **options):
        self.stdout.write("Create groups")
        admin_group, created = Group.objects.get_or_create(name="Admin")

        guest_group, created = Group.objects.get_or_create(name="Guest")

        content_type_posts = ContentType.objects.get_for_model(Post)
        post_permission = Permission.objects.filter(content_type=content_type_posts)
        for perm in post_permission:
            admin_group.permissions.add(perm)

        content_type_guest = ContentType.objects.get_for_model(Comment)
        guest_permission = Permission.objects.filter(content_type=content_type_guest)
        for perm in guest_permission:
            admin_group.permissions.add(perm)
            guest_group.permissions.add(perm)

        self.stdout.write(self.style.SUCCESS("Groups created"))

        super_user = User.objects.create_superuser(
            username='admin',
            first_name='Петр',
            last_name='Петрович',
            email='admin@ya.ru',
            password='12345')
        group = Group.objects.get(name="Admin")
        super_user.groups.add(group)
        self.stdout.write(self.style.SUCCESS(f"{super_user} added in Admin group"))

        for _ in range(20):
            person = Person(locale=Locale.RU)
            guest_user = User.objects.create_user(
                username=person.username(),
                first_name=person.first_name(gender=Gender.MALE),
                last_name=person.last_name(gender=Gender.MALE),
                email=person.email(),
                password='12345',

            )

            g_group = Group.objects.get(name="Guest")
            guest_user.groups.add(g_group)

            self.stdout.write(self.style.SUCCESS(f"{guest_user} added in Guest group"))

        self.stdout.write(self.style.SUCCESS("Process end successful."))

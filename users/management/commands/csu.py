from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        user = User.objects.create(
            email='vladislav_svintsitskiy@yandex.ru',
            first_name='Admin',
            last_name='Admini',
            is_active=True,
            is_staff=True,
            is_superuser=True
        )

        user.set_password('123qwe456rty')
        user.save()


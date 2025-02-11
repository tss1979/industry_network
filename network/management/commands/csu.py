from django.core.management import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='ad@ad.ru',
            username='admin',
            first_name='admin',
            last_name='admin',
            is_staff=True,
            is_superuser=True,
        )
        user.set_password('111')
        user.save()

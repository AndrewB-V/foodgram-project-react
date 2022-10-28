from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    user_data = {
        "username": "andrew",
        "email": "andrew@andrew.ru",
        "first_name": "Andrew",
        "last_name": "AndrewB",
    }
    user_password = "123qwe!@#"

    def handle(self, *args, **options):
        user, created = User.objects.get_or_create(**self.user_data)
        if created:
            user.is_superuser = True
            user.is_active = True
            user.is_staff = True
            user.set_password(self.user_password)
            user.save()

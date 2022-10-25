import json

from django.apps import AppConfig


class RecipesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'recipes'

    @classmethod
    def ready(cls):
        """ При миграциях, создаю суперпользователя, если он отсутствует.
            Также Ingredient.
        """

        from recipes.models import Ingredient
        from users.admin import User
        if not User.objects.filter(username="Dima").first():
            User.objects.create_superuser(
                username="Dima", email="dima@dima.ru", password="Dima")

        with open('ingredients.json', 'r', encoding='utf-8') as fh:
            # открываем файл на чтение
            data = json.load(fh)  # загружаем из файла данные в словарь data

        for i in data:
            bob, created = Ingredient.objects.get_or_create(
                name=i['name'], measurement_unit=i['measurement_unit'])

import json

from django.core.management import BaseCommand

from recipes.models import Ingredient


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open(
            "ingredients.json", "r", encoding="utf-8"
        ) as fh:  # открываем файл на чтение
            data = json.load(fh)  # загружаем из файла данные в словарь data

            for ingredient in data:
                ing, _ = Ingredient.objects.get_or_create(
                    name=ingredient.get("name"),
                    measurement_unit=ingredient.get("measurement_unit"),
                )

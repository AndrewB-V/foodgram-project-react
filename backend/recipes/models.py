from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models

from users.models import User


class Tag(models.Model):
    """Теги рецептов."""

    name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name='Название тега',
        help_text='Введите название тега'
    )
    color = models.CharField(
        max_length=7,
        blank=True,
        unique=True,
        verbose_name='Цвет в HEX',
        help_text='Введите цветовой код в hex-формате'
    )
    slug = models.SlugField(
        max_length=200,
        blank=True,
        unique=True,
        verbose_name='Уникальный префикс',
        help_text='Введите уникальный префикс'
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name[:50]


class Ingredient(models.Model):
    """Продукты."""

    name = models.CharField(
        max_length=200,
        verbose_name='Название ингредиента',
        db_index=True,
        help_text='Введите название ингредиента'
    )
    measurement_unit = models.CharField(
        max_length=200,
        verbose_name='Единица измерения',
        help_text='Введите единицу измерения ингредиента'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return f'{self.name}, {self.measurement_unit}'


class Recipe(models.Model):
    """Рецепты блюд."""

    name = models.CharField(
        max_length=200,
        db_index=True,
        verbose_name='Название рецепта'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор рецепта',
        help_text='Автор рецепта'
    )
    text = models.TextField(
        max_length=2048,
        verbose_name='Описание рецепта',
        help_text='Введите описание рецепта'
    )
    image = models.ImageField(
        upload_to='recipe/images',
        max_length=None,
        blank=True,
        null=True,
        verbose_name='Изображение для рецепта'
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='Теги рецепта',
        through='RecipeTag'
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        through='RecipeIngredient',
        verbose_name='Ингредиенты рецепта',
        help_text='Выберите продукты'
    )
    cooking_time = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1, message=settings.VALIDATOR_MESSAGE)
        ],
        verbose_name='Время приготовления (в минутах)',
        help_text='Время приготовления (в минутах)'
    )
    pub_date = models.DateTimeField(
        'Дата и время написания рецепта',
        auto_now_add=True
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name[:50]


class RecipeTag(models.Model):
    """Связывает рецепт и тэги"""

    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        verbose_name='Тэг',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепт',
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Тег рецепта'
        verbose_name_plural = 'Теги рецепта'
        constraints = (
            models.UniqueConstraint(fields=('tag', 'recipe'),
                                    name='unique_tag_recipes'),
        )


class RecipeIngredient(models.Model):
    """Ингредиенты блюда."""

    recipe_id = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Название рецепта',
        help_text='Название рецепта'
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        verbose_name='Ингредиент',
        help_text='Название ингредиента'
    )
    amount = models.PositiveSmallIntegerField(
        default=1,
        validators=[
            MinValueValidator(1, message=settings.VALIDATOR_MESSAGE)
        ],
        verbose_name='Количество ингредиентов',
        help_text='Количество ингредиентов'
    )

    class Meta:
        verbose_name = 'Рецепт и ингредиент'
        verbose_name_plural = 'Рецепт и ингредиенты'
        constraints = (
            models.UniqueConstraint(fields=('ingredient', 'recipe_id'),
                                    name='unique_ingredients_recipes'),
        )

    def __str__(self):
        return f'{self.ingredient} - {self.amount}'


class Favorites(models.Model):
    """Избранные рецепты."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='subscriber',
        verbose_name='Подписчик',
        help_text='Имя подписчика'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name='Избранный рецепт',
        help_text='Избранный рецепт'
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'
        constraints = (
            models.UniqueConstraint(fields=('user', 'recipe'),
                                    name='unique_favorite'),
        )

    def __str__(self):
        return f'{self.user} - {self.recipe}'


class ShoppingCart(models.Model):
    """Список покупок."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='cart_user',
        verbose_name='Пользователь',
        help_text='Имя пользователя'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='cart_recipe',
        verbose_name='Рецепт',
        help_text='Рецепт в списке покупок'
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'
        constraints = (
            models.UniqueConstraint(fields=('user', 'recipe'),
                                    name='unique_shopping_cart'),
        )

    def __str__(self):
        return f'{self.user} - {self.recipe}'


class Follow(models.Model):
    """Система подписок на отдельных авторов"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик',
        help_text='Имя подписчика'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор рецепта',
        help_text='Имя автора рецепта'
    )

    class Meta:
        verbose_name = 'Подписки'
        verbose_name_plural = 'Подписки'
        constraints = [
            models.UniqueConstraint(fields=('user', 'author'),
                                    name='unique_follow'),
        ]

    def __str__(self):
        return f'{self.user} - {self.author}'

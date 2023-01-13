from rest_framework import serializers

from src.ingredients.models import Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    """Вывод информации о ингредиенте."""

    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'measurement_unit')

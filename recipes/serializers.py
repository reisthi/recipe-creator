from rest_framework import serializers

from users.models import User
from .models import Recipe, Ingredient, Step


class StepSerializer(serializers.HyperlinkedModelSerializer):
    recipe = serializers.PrimaryKeyRelatedField(queryset=Recipe.objects.all(), source='recipe.name')

    class Meta:
        model = Step
        fields = ['step_text', 'recipe', 'url', ]

    def create(self, validated_data):
        subject = Step.objects.create(recipe=validated_data['recipe']['name'], step_text=validated_data['step_text'])
        return subject

    def update(self, instance, validated_data):
        """
        Update and return an existing `Step` instance, given the validated data.
        """
        instance.step_text = validated_data.get('step_text', instance.step_text)
        instance.recipe.name = validated_data.get('recipe', instance.recipe)
        instance.save()
        return instance


class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    recipe = serializers.PrimaryKeyRelatedField(queryset=Recipe.objects.all(), source='recipe.name')

    class Meta:
        model = Ingredient
        fields = ['name', 'recipe', 'url', ]

    def create(self, validated_data):
        subject = Ingredient.objects.create(recipe=validated_data['recipe']['name'], name=validated_data['name'])
        return subject

    def update(self, instance, validated_data):
        """
        Update and return an existing `Ingredient` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.recipe.name = validated_data.get('recipe', instance.recipe)
        instance.save()
        return instance


class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user.username')
    ingredients = IngredientSerializer(many=True, read_only=True)
    steps = StepSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = ('name', 'user', 'ingredients', 'steps', 'url',)

    def create(self, validated_data):
        subject = Recipe.objects.create(user=validated_data['user']['username'], name=validated_data['name'])
        return subject

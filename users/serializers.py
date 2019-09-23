from recipes.serializers import RecipeSerializer
from .models import User
from rest_framework import serializers


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'recipes']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    recipes = RecipeSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'url', 'recipes',)

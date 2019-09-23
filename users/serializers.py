from recipes.serializers import RecipeSerializer
from rest_framework import serializers

from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    recipes = RecipeSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'url', 'recipes',)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user

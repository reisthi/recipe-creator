from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=255, null=False)
    user = models.ForeignKey('users.User', related_name='recipes', on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Step(models.Model):
    step_text = models.CharField(null=False, max_length=500)
    recipe = models.ForeignKey(Recipe, related_name='steps', on_delete=models.CASCADE)

    def __str__(self):
        return self.step_text


class Ingredient(models.Model):
    name = models.CharField(null=False, max_length=500)
    recipe = models.ForeignKey(Recipe, related_name='ingredients', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

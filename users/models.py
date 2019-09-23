from django.contrib.auth.models import AbstractUser
from django.db import models

from recipes.models import Recipe


class User(AbstractUser):
    email = models.EmailField(unique=True)

    class Meta:
        ordering = ('first_name',)

    def __str__(self):
        return self.username

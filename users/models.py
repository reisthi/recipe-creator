from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.db import models

from recipes.models import Recipe


class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(_('password'), max_length=128)

    class Meta:
        ordering = ('id',)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

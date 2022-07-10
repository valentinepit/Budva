from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    password = models.CharField(max_length=40)

    def get_absolute_url(self):
        return reverse('users:users_list')

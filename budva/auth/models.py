from django.contrib.auth.models import AbstractUser
from django.db import models

from budva.points.models import Points


class User(AbstractUser):
    traces = models.ManyToManyField(Points, verbose_name='users_traces')

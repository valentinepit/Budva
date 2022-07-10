from django.db import models
from django.urls import reverse
from points.models import Points

from users.models import User


class Traces(models.Model):
    title = models.CharField(max_length=255, blank=True)
    points = models.ManyToManyField(Points, related_name='included_points', blank=True)
    distance = models.FloatField(verbose_name='Distance')
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('traces:trace_detail', args=[str(self.id)])



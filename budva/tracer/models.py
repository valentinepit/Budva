from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.urls import reverse

from points.models import Points


class Traces(models.Model):
    title = models.CharField(max_length=255, blank=True)
    points = models.ManyToManyField(Points, related_name='included_points', blank=True)
    distance = models.FloatField(verbose_name='Distance')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('traces:trace_detail', args=[str(self.id)])


# @receiver(post_save, sender=Traces)
# def my_callback(sender, instance, *args, **kwargs):
#     print(f"{Traces.objects.filter(id=28).points = }")
#
#
# @receiver(pre_save, sender=Traces)
# def my_callback(sender, instance, *args, **kwargs):
#     instance.id = Traces.objects.all().last().id + 1
#     instance.distance = 20
#     print(f"{instance.points.prefetch_related() = }")

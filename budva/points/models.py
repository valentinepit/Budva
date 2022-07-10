from django.db import models
from django.urls import reverse


class Points(models.Model):
    name = models.CharField(max_length=255, verbose_name="name", blank=False)
    abscissa = models.FloatField(verbose_name="x", blank=False)
    ordinata = models.FloatField(verbose_name="y", blank=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("points:point_detail", args=[str(self.id)])

from django.db import models
from django.urls import reverse
from points.models import Points
from sortedm2m.fields import SortedManyToManyField

from users.models import User


class Traces(models.Model):
    title = models.CharField(max_length=255, blank=True)
    # К сожалению данное поле не работает так как в документации.
    points = SortedManyToManyField(Points, related_name="included_points", blank=False, sorted=False)
    distance = models.FloatField(verbose_name="Distance")
    user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE, null=True)
    break_points = models.CharField(max_length=100, blank=True)

    def set_break_points(self, x):
        self.break_points = json.dumps(x)

    def get_break_points(self):
        print(f"{self.break_points = }")
        return json.loads(self.break_points)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("traces:trace_detail", args=[str(self.id)])

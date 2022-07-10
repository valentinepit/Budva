from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [

    path("admin/", admin.site.urls),
    path('', views.index),
    path("points/", include("points.urls", namespace="points")),
    path("traces/", include("tracer.urls", namespace="traces")),
    path("users/", include("users.urls", namespace="users")),
]


from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('points/', include('points.urls', namespace='points')),
    path('traces/', include('tracer.urls', namespace='traces')),
]

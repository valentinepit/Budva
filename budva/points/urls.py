
from django.urls import path
from . import views as points

app_name = 'points'

urlpatterns = [
    path('', points.PointsListView.as_view(), name='point_list'),
    path('create/', points.CreatePointView.as_view(), name='point_create'),
    path('post/<int:pk>/', points.PointsDetailView.as_view(), name='point_detail'),
    path('update/<int:pk>/', points.PointsUpdateView.as_view(), name='point_edit'),
    path('delete/<int:pk>/', points.PointsDeleteView.as_view(), name='point_delete'),
]

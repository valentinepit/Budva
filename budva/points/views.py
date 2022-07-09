import point as point
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, ListView

from .models import Points


class CreatePointView(CreateView):
    model = Points
    template_name = 'points/points_create.html'
    fields = ['name', 'abscissa', 'ordinata']


class PointsDeleteView(DeleteView):
    model = Points
    template_name = 'points/points_delete.html'
    success_url = reverse_lazy('points:point_list')


class PointsUpdateView(UpdateView):
    model = Points
    template_name = 'points/points_update.html'
    fields = ['name']


class PointsListView(ListView):
    model = Points
    template_name = 'points/points_list.html'

    def get_context_data(self, **kwargs):
        context = super(PointsListView, self).get_context_data(**kwargs)
        points = Points.objects.all()
        context.update({
            'points': points,
        })
        return context


class PointsDetailView(DeleteView):
    model = Points
    template_name = 'points/points_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PointsDetailView, self).get_context_data(**kwargs)
        _point = context.get('object')
        context.update({
            'point': _point,
        })
        return context

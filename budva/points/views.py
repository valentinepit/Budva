from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, ListView

from .models import Points


class CreatePointView(LoginRequiredMixin, CreateView):
    model = Points
    template_name = 'points/points_create.html'
    fields = ['name', 'abscissa', 'ordinata']
    login_url = 'users:login'
    redirect_field_name = 'redirect_to'


class PointsDeleteView(LoginRequiredMixin, DeleteView):
    model = Points
    template_name = 'points/points_delete.html'
    success_url = reverse_lazy('points:point_list')
    login_url = 'users:login'
    redirect_field_name = 'redirect_to'


class PointsUpdateView(LoginRequiredMixin, UpdateView):
    model = Points
    template_name = 'points/points_update.html'
    fields = ['name']
    login_url = 'users:login'
    redirect_field_name = 'redirect_to'


class PointsListView(LoginRequiredMixin, ListView):
    model = Points
    template_name = 'points/points_list.html'
    login_url = 'users:login'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super(PointsListView, self).get_context_data(**kwargs)
        points = Points.objects.all()
        context.update({
            'points': points,
        })
        return context


class PointsDetailView(LoginRequiredMixin, DeleteView):
    model = Points
    template_name = 'points/points_detail.html'
    login_url = 'users:login'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super(PointsDetailView, self).get_context_data(**kwargs)
        _point = context.get('object')
        context.update({
            'point': _point,
        })
        return context

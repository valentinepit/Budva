from math import sqrt
from turtle import distance

from django.db.models.signals import post_save
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.dispatch import receiver

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

from .forms import TraceCreateForm
from .models import Traces
from points.models import Points


class TracesListView(ListView):
    model = Traces
    template_name = 'tracer/traces_list.html'



class TracesCreateView(CreateView):
    model = Traces
    form_class = TraceCreateForm
    distance = 0


    def get_form_kwargs(self):
        kwargs = super(TracesCreateView, self).get_form_kwargs()
        return kwargs["data"].getlist("points")

# def form_valid(self, form):
#     instance = form.instance
#     instance.id = Traces.objects.all().last().id + 1
#     print(f"{instance.points.all() =}")
#     return super().form_valid(form)


    def post(self, request, *args, **kwargs):
        form = TraceCreateForm(request.POST)
        _id = 1 if not Traces.objects.all().last() else Traces.objects.all().last().id + 1
        if form.is_valid():
            if form.is_valid():
                instance = form.instance
                instance.distance = 20
                instance.id = _id
                form.save()
                for point in Points.objects.filter(pk__in=self.get_form_kwargs()):
                    instance.points.add(point)
            return HttpResponseRedirect('/traces/')
        return reverse_lazy('traces:traces_list')

# def get_queryset(self):
#     queryset = super().get_queryset().select_related()
#     print(f"{queryset = }")
#     return Traces.objects.all()

# @receiver(post_save, sender=Traces)
# def calculate_distance(self, _data, **kwargs):
#     dist = 0
#     print(**kwargs)
#     # for _point in _data.points.all():
#     print(f"{_data.points.select_related() =}")
#     return 20

# def create_trace(request):
#     if request.method == "POST":
#         trace = Traces()
#         print(request.POST)
#         trace.title = request.POST.get("title")
#         print(request.POST.getlist("points"))
#         points = request.POST.get("points")
#         trace.points, trace.distance = calculate_distance(points)
#         # trace.id = Traces.objects.last().id + 1
#         # trace.distance = 20
#         trace.save()
#         return HttpResponseRedirect("/tracers/")
#     context = {
#         "points": Points.objects.all()
#     }
#
#     return render(request, 'tracer/traces_create.html', context)
#
#
# def calculate_distance(_points):
#     dst = 0
#     pts = []
#     pts = Points.objects.filter(id__in=_points).order_by('abscissa')
#     # for point in pts:
#     #     dst += sqrt(point.abscissa)
#     for pt in pts:
#         print(pt.abscissa)
#     return pts, dst


class TraceDetailView(DetailView):
    model = Traces
    template_name = 'tracer/trace_detail.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(TraceDetailView, self).get_context_data(**kwargs)
        points = kwargs.get("object").points.all()
        context.update({
            'points': points,
        })
        return context


class TraceDeleteView(DeleteView):
    model = Traces
    template_name = 'tracer/trace_delete.html'
    success_url = reverse_lazy('traces:traces_list')


class TraceUpdateView(UpdateView):
    model = Traces
    template_name = 'tracer/trace_update.html'
    fields = '__all__'

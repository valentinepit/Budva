from math import sqrt
import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from points.models import Points

from .forms import TraceCreateForm
from .models import Traces


def index(request):
    context = {}
    return render(request, "tracer/index.html", context)


class TracesListView(LoginRequiredMixin, ListView):
    model = Traces
    template_name = "tracer/traces_list.html"
    login_url = "users:login"
    redirect_field_name = "redirect_to"


class TracesCreateView(LoginRequiredMixin, CreateView):
    model = Traces
    form_class = TraceCreateForm
    login_url = "users:login"
    redirect_field_name = "redirect_to"

    def get_form_kwargs(self):
        kwargs = super(TracesCreateView, self).get_form_kwargs()
        try:
            return kwargs["data"].getlist("points")
        except KeyError:
            return kwargs

    def post(self, request, *args, **kwargs):
        form = TraceCreateForm(request.POST)
        _id = 1 if not Traces.objects.last() else Traces.objects.last().id + 1
        if form.is_valid():
            if form.is_valid():
                instance = form.instance
                points = Points.objects.filter(pk__in=self.get_form_kwargs()).order_by("abscissa")
                instance.distance = self.get_distance(points)
                instance.id = _id
                form.save()
                break_points = []
                for point in points:
                    instance.points.add(point)
                    break_points.append(point.id)
                instance.break_points = break_points
                instance.save()
            return HttpResponseRedirect("/traces/")
        return HttpResponseRedirect("/traces/")

    def get_distance(self, pts):
        dst = 0
        for i in range(len(pts) - 1):
            dst += sqrt((pts[i + 1].abscissa - pts[i].abscissa) ** 2 + (pts[i + 1].abscissa - pts[i].abscissa) ** 2)
        return dst


class TraceDetailView(LoginRequiredMixin, DetailView):
    model = Traces
    template_name = "tracer/trace_detail.html"
    fields = "__all__"
    login_url = "users:login"
    redirect_field_name = "redirect_to"

    def get_context_data(self, **kwargs):
        context = super(TraceDetailView, self).get_context_data(**kwargs)
        break_points = json.loads(kwargs.get("object").break_points)
        # INFO  Чтобы сохранить порядок точек, а не просто выводить их отсортированными по координатом
        points = self.get_points(break_points)
        context.update({"points": points})
        return context

    def get_points(self, bp):
        pts = []
        for pk in bp:
            pts.append(Points.objects.filter(pk=pk).last())
        return pts


class TraceDeleteView(LoginRequiredMixin, DeleteView):
    model = Traces
    template_name = "tracer/trace_delete.html"
    success_url = reverse_lazy("traces:traces_list")
    login_url = "users:login"
    redirect_field_name = "redirect_to"


class TraceUpdateView(LoginRequiredMixin, UpdateView):
    model = Traces
    template_name = "tracer/trace_update.html"
    fields = "__all__"
    login_url = "users:login"
    redirect_field_name = "redirect_to"

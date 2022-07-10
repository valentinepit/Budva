from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from users.forms import UserCreateForm, UserLoginForm
from users.models import User

from tracer.models import Traces


class UsersCreateView(CreateView):
    model = User
    form_class = UserCreateForm
    login_url = "traces:index"
    redirect_field_name = "redirect_to"


class UsersListView(LoginRequiredMixin, ListView):
    model = User
    template_name = "users/users_list.html"
    login_url = "users:login"
    redirect_field_name = "redirect_to"


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "users/users_detail.html"
    fields = "__all__"
    login_url = "users:login"
    redirect_field_name = "redirect_to"

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        # traces = kwargs.get("object").traces.all()
        user_id = kwargs.get("object").id
        traces = Traces.objects.filter(user__pk=user_id)
        distance_sum = 0
        for trace in traces:
            distance_sum += trace.distance
        context.update({"traces": traces, "distance_sum": distance_sum})
        return context


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = "users/user_update.html"
    fields = "__all__"
    login_url = "users:login"
    redirect_field_name = "redirect_to"


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = "users/user_delete.html"
    login_url = "users:login"
    redirect_field_name = "redirect_to"


def login(request):
    login_form = UserLoginForm(data=request.POST)
    next_param = request.GET.get("next", "")
    if request.method == "POST" and login_form.is_valid():
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            if "next" in request.POST.keys():
                return HttpResponseRedirect(request.POST["next"])
            return HttpResponseRedirect(reverse("traces:index"))

    context = {
        "login_form": login_form,
        "next_param": next_param,
    }

    return render(request, "users/login.html", context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("traces:index"))

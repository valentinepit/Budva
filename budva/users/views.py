from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from users.forms import UserCreateForm, UserLoginForm
from users.models import User



class UsersCreateView(CreateView):
    model = User
    form_class = UserCreateForm


class UsersListView(ListView):
    model = User
    template_name = 'users/users_list.html'


class UserDetailView(DetailView):
    model = User
    template_name = 'users/users_detail.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        traces = kwargs.get("object").traces.all()
        context.update({
            'traces': traces,
        })
        return context


class UserUpdateView(UpdateView):
    model = User
    template_name = 'users/user_update.html'
    fields = '__all__'


class UserDeleteView(DeleteView):
    model = User
    template_name = 'users/user_delete.html'


def login(request):
    login_form = UserLoginForm(data=request.POST)
    next_param = request.GET.get('next', '')
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            if 'next' in request.POST.keys():
                return HttpResponseRedirect(request.POST['next'])
            return HttpResponseRedirect(reverse('traces:index'))

    context = {
        'login_form': login_form,
        'next_param': next_param,
    }

    return render(request, 'users/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('traces:index'))

from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from users.forms import UserCreateForm
from users.models import User


class UsersCreateView(CreateView):
    model = User
    # template_name = 'users/user_create.html'
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
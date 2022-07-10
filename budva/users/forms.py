from django.forms import ModelForm

from .models import User


class UserCreateForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

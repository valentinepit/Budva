from django import forms
from django.forms import ModelForm

from .models import Traces
from points.models import Points


class TraceCreateForm(ModelForm):
    points = forms.ModelMultipleChoiceField(queryset=Points.objects.all(), widget=forms.CheckboxSelectMultiple,
                                            required=True)

    class Meta:
        model = Traces
        fields = ['title', 'points', 'user']

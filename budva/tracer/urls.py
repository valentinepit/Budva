from django.urls import path
from . import views as traces

app_name = "traces"

urlpatterns = [
    path("", traces.index, name="index"),
    path("traces/", traces.TracesListView.as_view(), name="traces_list"),
    path("create/", traces.TracesCreateView.as_view(), name="traces_create"),
    path("trace/<int:pk>/", traces.TraceDetailView.as_view(), name="trace_detail"),
    path("update/<int:pk>/", traces.TraceUpdateView.as_view(), name="trace_edit"),
    path("delete/<int:pk>/", traces.TraceDeleteView.as_view(), name="trace_delete"),
]

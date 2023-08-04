from django.urls import path
from .views_front import (
    DailypulseCreateView,
    DailypulseDeleteView,
    DailypulseDetailView,
    DailypulseListView,
    DailypulseUpdateView,
)

urlpatterns = [
    path("", DailypulseListView.as_view(), name="dailypulse_list"),
    path("<int:pk>/", DailypulseDetailView.as_view(), name="dailypulse_detail"),
    path("create/", DailypulseCreateView.as_view(), name="dailypulse_create"),
    path("<int:pk>/update/", DailypulseUpdateView.as_view(), name="dailypulse_update"),
    path("<int:pk>/delete/", DailypulseDeleteView.as_view(), name="dailypulse_delete"),
]

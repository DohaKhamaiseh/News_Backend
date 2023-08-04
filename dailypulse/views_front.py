from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Dailypulse


class DailypulseListView(LoginRequiredMixin, ListView):
    template_name = "dailypulses/dailypulse_list.html"
    model = Dailypulse
    context_object_name = "dailypulses"


class DailypulseDetailView(LoginRequiredMixin, DetailView):
    template_name = "dailypulse/dailypulse_detail.html"
    model = Dailypulse


class DailypulseUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "dailypulse/dailypulse_update.html"
    model = Dailypulse
    fields = "__all__"


class DailypulseCreateView(LoginRequiredMixin, CreateView):
    template_name = "dailypulse/dailypulse_create.html"
    model = Dailypulse
    fields =  "__all__"


class DailypulseDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "dailypulse/dailypulse_delete.html"
    model = Dailypulse
    success_url = reverse_lazy("dailypulse_list")

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from django.urls import reverse_lazy

from .models import Reading


class ReadingList(ListView):
    model = Reading
    context_object_name = "readings"


class ReadingDetail(DetailView):
    model = Reading
    context_object_name = "reading"


class ReadingCreate(CreateView):
    model = Reading
    fields = "__all__"
    success_url = reverse_lazy("list")
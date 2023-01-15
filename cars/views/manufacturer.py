from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from cars.models import Manufacturer
from django.views.generic import (CreateView, ListView, DetailView, UpdateView, DeleteView)


class ManufacturerCreateView(CreateView):
    model = Manufacturer
    fields = "__all__"
    template_name = "manufacturer/create.html"

    def get_success_url(self):
        return reverse("manufacturer-detail", args=[self.object.pk])


class ManufacturerListView(ListView):
    model = Manufacturer
    context_object_name = "manufacturers"
    template_name = "manufacturer/list.html"


class ManufacturerDetailView(DetailView):
    model = Manufacturer
    template_name = "manufacturer/detail.html"


class ManufacturerUpdateView(UpdateView):
    model = Manufacturer
    fields = "__all__"
    template_name = "manufacturer/update.html"

    def get_success_url(self):
        return reverse("manufacturer-detail", args=[self.object.pk])


class ManufacturerDeleteView(DeleteView):
    pass
    model = Manufacturer
    success_url = reverse_lazy("manufacturer-list")

    def get(self, request, *args, **kwargs):
        return redirect("manufacturer-list-list")







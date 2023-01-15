from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from cars.models import Make
from django.views.generic import (CreateView, ListView, DetailView, UpdateView, DeleteView)


class MakeCreateView(CreateView):
    model = Make
    fields = "__all__"
    template_name = "make/create.html"

    def get_success_url(self):
        return reverse("make-detail", args=[self.object.pk])


class MakeListView(ListView):
    model = Make

    context_object_name = "makes"
    template_name = "make/list.html"


class MakeDetailView(DetailView):
    model = Make
    template_name = "make/detail.html"


class MakeUpdateView(UpdateView):
    model = Make
    fields = "__all__"

    def get_success_url(self):
        return reverse("make-detail", args=[self.object.id])

    template_name = "make/update.html"


class MakeDeleteView(DeleteView):
    model = Make
    success_url = reverse_lazy("make-list")

    def get(self, request, *args, **kwargs):
        return redirect("book-list")

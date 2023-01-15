from django.urls import path
from .views import make, manufacturer


urlpatterns = [
    path("manufacturer/create", manufacturer.ManufacturerCreateView.as_view(), name="manufacturer-create"),
    path("manufacturers/", manufacturer.ManufacturerListView.as_view(), name="manufacturer-list"),
    path("manufacturers/<int:pk>", manufacturer.ManufacturerDetailView.as_view, name="manufacturer-detail"),
    path("manufacturers/<int:pk>/update/", manufacturer.ManufacturerUpdateView.as_view(), name="manufacturer-update"),
    path("manufacturers/<int:pk>/delete/", manufacturer.ManufacturerDeleteView.as_view(), name="manufacturer-delete"),

    path("make/create", make.MakeCreateView.as_view(), name="make-create"),
    path("makes/", make.MakeListView.as_view(), name="make-list"),
    path("makes/<int:pk>", make.MakeDetailView.as_view(), name='make-detail'),
    path("makes/<int:pk>/update", make.MakeUpdateView.as_view(), name="make-update"),
    path("makes/<int:pk>/delete", make.MakeDeleteView.as_view(), name="make-delete"),

]
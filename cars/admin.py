from django.contrib import admin
from .models import Manufacturer, Make

# Register your models here.
admin.site.register(Manufacturer)
admin.site.register(Make)

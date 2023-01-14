from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    brand_creation_date = models.DateField()
    picture = models.ImageField(upload_to="author/", blank=True, null=True)

    def __str__(self):
        return self.name


class Make(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    engine_vol = models.FloatField(max_length=100)
    release_date = models.DateField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name="make")

    def __str__(self):
        return self.name

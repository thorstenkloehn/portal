from django.contrib.gis.db import models


# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    location = models.PointField(geography=True, srid=4326)

    def __str__(self):
        return self.name
import datetime
from django.db import models
from .user import User

class Hike(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    date = models.DateField(("Date"), default=datetime.date.today)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

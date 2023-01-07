import datetime
from django.db import models
from .user import User

class Hike(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    hike_location = models.URLField(max_length=200)
    date = models.DateField(("Date"), default=datetime.date.today)
    description = models.CharField(max_length=1000)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

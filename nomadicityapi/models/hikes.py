import datetime
from django.db import models
from .users import User
from .boards import Board

class Hike(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_hike')
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    url = models.URLField(max_length=200)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    description = models.CharField(max_length=1000)
    objects = models.Manager()



    def __str__(self):
        return self.name

import datetime
from django.db import models
from .user import User

class Board(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image_url = models.URLField(max_length=200)
    state = models.TextField(max_length=100)
    description = models.TextField(max_length=1000)
    types = models.TextField(max_length=100)
    objects = models.Manager()

    def __str__(self):
        return self.name

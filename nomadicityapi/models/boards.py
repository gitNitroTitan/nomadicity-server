from django.db import models
from .users import User

class Board(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_board')
    title = models.CharField(max_length=50)
    image_url = models.URLField(max_length=200)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

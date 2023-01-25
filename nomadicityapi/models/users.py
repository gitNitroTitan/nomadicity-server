from django.db import models

class User(models.Model):
    uid = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.CharField(max_length=1000)
    profile_image_url = models.URLField(max_length=200)
    email = models.EmailField(max_length=254)

    @property
    def hikes(self):
        """user hikes"""
        hikes = [hike for hike in self.user_hike.all()]
        return hikes

    @property
    def boards(self):
        """user hikes"""
        boards = [board for board in self.user_board.all()]
        return boards


    def __str__(self):
        return self.first_name + self.last_name

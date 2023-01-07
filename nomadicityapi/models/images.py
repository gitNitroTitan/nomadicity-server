from django.db import models
from nomadicityapi.models import Hike


class HikeImage(models.Model):
    hike = models.ForeignKey(Hike, on_delete=models.DO_NOTHING, related_name='pictures')
    action_pic = models.ImageField(
        upload_to='actionimages', height_field=None,
        width_field=None, max_length=None, null=True)

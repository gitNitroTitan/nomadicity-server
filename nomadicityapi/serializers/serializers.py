from rest_framework.serializers import ModelSerializer
from nomadicityapi.models import Hike, Board, User

class HikeSerializer(ModelSerializer):
  """JSON serializer for hikes"""
  class Meta:
    model= Hike
    fields = ( 'id', 'user', 'board', 'name', 'url', 'latitude', 'longitude', 'description')
    depth = 2

class BoardSerializer(ModelSerializer):
    """JSON serializer for boards
    """
    class Meta:
        model = Board
        fields = ('id', 'user', 'title',
                'image_url', 'description')
        depth = 2
class UserSerializer(ModelSerializer):
    """"JSON serializer for users"""
    boards= BoardSerializer(many=True)
    hikes= HikeSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'uid', 'first_name', 'last_name', 'bio', 'profile_image_url', 'email', 'hikes', 'boards')

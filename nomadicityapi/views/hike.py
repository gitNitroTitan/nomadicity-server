from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from nomadicityapi.models import Board, Hike, User
from rest_framework.decorators import action
from rest_framework import generics
from django.shortcuts import get_object_or_404

class HikeSerializer(serializers.ModelSerializer):
  """JSON serializer for comments"""
  class Meta:
    model= Hike
    fields = ( 'id', 'board', 'name', 'url', 'latitude', 'longitude', 'description')
    depth = 2

class HikeView(ViewSet):
  """ Nomadicity Hikes view"""

  def retrieve(self, request, pk):
    """Handles GET requests for single comment
    Returns:
      Response -- JSON serialized comment
    """
    hike = Hike.objects.get(pk=pk)
    serializer = HikeSerializer(hike)
    return Response(serializer.data)

  def list(self, request):
      """Handle GET requests to get all hikes for board and the name

      Returns:
          Response -- JSON serialized list of hikes
      """
      hikes = Hike.objects.all()

      # user = request.query_params.get('user', None)
      # if user is not None:
      #   hikes = hikes.filter(uid=user.uid)
      board = request.query_params.get('board', None)
      if board is not None:
        hikes = hikes.filter(board_id=board)
      serializer = HikeSerializer(hikes, many=True)

      return Response(serializer.data)

  def create(self, request):
      """Handle POST operations

      Returns
          Response -- JSON serialized comment instance
      """
      user = User.objects.get(uid = request.data["user"])
      board = Board.objects.get(pk = request.data["board"])

      hike = Hike.objects.create(
          name = request.data["name"],
          url = request.data["url"],
          latitude = request.data["latitude"],
          longitude = request.data["longitude"],
          description = request.data["description"],
          user = user,
          board = board
      )
      serializer = HikeSerializer(hike)
      return Response(serializer.data)

  def update(self, request, pk):
    """Handle PUT requests for a comment

    Returns:
        Response -- Empty body with 204 status code
    """
    board = Board.objects.get(pk = request.data["board"])

    hike = Hike.objects.get(pk=pk)
    hike.description = request.data["description"]
    hike.latitude = request.data["latitude"]
    hike.longitude = request.data["longitude"]
    board = Board.objects.get(pk=request.data["board"])
    hike.board = board

    hike.save()
    return Response(None, status=status.HTTP_204_NO_CONTENT)

  def destroy(self, request, pk):
    hike = Hike.objects.get(pk=pk)
    hike.delete()

    return Response(None, status=status.HTTP_204_NO_CONTENT)

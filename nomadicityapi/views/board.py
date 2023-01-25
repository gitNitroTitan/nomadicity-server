from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from nomadicityapi.models import Board, Hike, User
from nomadicityapi.serializers import BoardSerializer
from rest_framework.decorators import action

class BoardView(ViewSet):

    def retrieve(self, request, pk):
        board = Board.objects.get(pk=pk)
        serializer = BoardSerializer(board)
        return Response(serializer.data)

    def list(self, request):
        boards = Board.objects.all()

        serializer = BoardSerializer(boards, many=True)
        return Response(serializer.data)


    def create(self, request):
        """Handle create requests for board
        """
        user = User.objects.get(uid=request.data["user"])

        board = Board.objects.create(
                title=request.data["title"],
                image_url=request.data["image_url"],
                description=request.data["description"],
                user=user
            )
        serializer = BoardSerializer(board)
        return Response(serializer.data)

    def update(self, request, pk):

        board = Board.objects.get(pk=pk)
        board.title=request.data["title"]
        board.image_url=request.data["image_url"]
        board.description=request.data["description"]
        board.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        board = Board.objects.get(pk=pk)
        board.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

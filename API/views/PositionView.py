from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from API.models import Position
from API.serializers import PositionSerializer


class PositionView(APIView):
    serializer_class = PositionSerializer
    queryset = Position.objects.all()

    def get(self, request: Request, format=None) -> Response:
        serializer = self.serializer_class(self.queryset.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request, format=None, *args, **kwargs) -> Response:
        serializer = self.serializer_class(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PositionDetailView(APIView):
    serializer_class = PositionSerializer

    def get(self, request: Request, pk: int, format=None) -> Response:
        position = get_object_or_404(Position, pk=pk)
        serializer = self.serializer_class(position)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request: Request, pk: int, format=None, *args, **kwargs) -> Response:
        serializer = self.serializer_class(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request: Request, pk: int, format=None, *args, **kwargs) -> Response:
        serializer = self.serializer_class(request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk: int, format=None, *args, **kwargs) -> Response:
        position = get_object_or_404(Position, pk=pk)
        position.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

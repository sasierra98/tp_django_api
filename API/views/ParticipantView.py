from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from API.models import Participant
from API.serializers import ParticipantSerializer


class ParticipantView(APIView):
    serializer_class = ParticipantSerializer
    queryset = Participant.objects.all()

    def get(self, request: Request, format=None) -> Response:
        serializer = self.serializer_class(self.queryset.all().order_by('id'), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request, format=None, *args, **kwargs) -> Response:
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ParticipantDetailView(APIView):
    serializer_class = ParticipantSerializer

    def get(self, request: Request, pk: int, format=None) -> Response:
        competition = get_object_or_404(Participant, pk=pk)
        serializer = self.serializer_class(competition)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request: Request, pk: int, format=None, *args, **kwargs) -> Response:
        competition = get_object_or_404(Participant, pk=pk)
        serializer = self.serializer_class(competition, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request: Request, pk: int, format=None, *args, **kwargs) -> Response:
        competition = get_object_or_404(Participant, pk=pk)
        serializer = self.serializer_class(competition, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk: int, format=None, *args, **kwargs) -> Response:
        competition = get_object_or_404(Participant, pk=pk)
        competition.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

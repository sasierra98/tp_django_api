from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from API.models import Employee
from API.serializers import ConsultantSerializer


class EmployeeView(APIView):
    serializer_class = ConsultantSerializer
    queryset = Employee.objects.all()

    def get(self, request: Request, format=None) -> Response:
        serializer = self.serializer_class(self.queryset.all().order_by('id'), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request, format=None, *args, **kwargs) -> Response:
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeDetailView(APIView):
    serializer_class = ConsultantSerializer

    def get(self, request: Request, pk: int, format=None) -> Response:
        consultant = get_object_or_404(Employee, pk=pk)
        serializer = self.serializer_class(consultant)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request: Request, pk: int, format=None, *args, **kwargs) -> Response:
        consultant = get_object_or_404(Employee, pk=pk)
        serializer = self.serializer_class(consultant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request: Request, pk: int, format=None, *args, **kwargs) -> Response:
        consultant = get_object_or_404(Employee, pk=pk)
        serializer = self.serializer_class(consultant, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk: int, format=None, *args, **kwargs) -> Response:
        consultant = get_object_or_404(Employee, pk=pk)
        consultant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

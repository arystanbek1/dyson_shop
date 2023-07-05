from rest_framework import status
from rest_framework.response import Response
from .models import *
from rest_framework.views import APIView
from .serializers import *


class DysonAPI(APIView):
    def get(self, request, *args, **kwargs):
        dyson_model = DysonModel.objects.filter(delete=False)
        serializer = DysonSerializer(dyson_model, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = DysonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"message": "New record created", "data": serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DysonDetailView(APIView):
    def get(self, request, pk, *args, **kwargs):
        dyson_model = DysonModel.objects.get(pk=pk)
        serializer = DysonDetailSerializer(dyson_model, read_only=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, *args, **kwargs):
        dyson_model = DysonModel.objects.get(pk=pk)
        serializer = DysonUpdateDetailSerializer(dyson_model, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"message": "Record updated", "data": serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        dyson_model = DysonModel.objects.filter(pk=pk, delete=False)
        if dyson_model:
            dyson_model[0].delete = True
            dyson_model[0].save()
            return Response(data={"message": "Record deleted"}, status=status.HTTP_200_OK)
        else:
            return Response(data={"message": "Record doenst exist"}, status=status.HTTP_404_NOT_FOUND)





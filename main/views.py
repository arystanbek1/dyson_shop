from rest_framework import status
from rest_framework.response import Response
from .models import DysonModel
from rest_framework.views import APIView
from .serializers import DysonSerializer


class DysonAPI(APIView):
    def get(self, request, *args, **kwargs):
        dyson_model = DysonModel.objects.all()
        serializer = DysonSerializer(dyson_model, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        new_dyson = DysonModel(
            name=request.data['name'],
            image=request.data['image'],
            articul=request.data['articul'],
            price=request.data['price'],
            country=request.data['country'],
            characteristic=request.data['characteristic'],
            color=request.data['color'],
            cap=request.data['cap'],
            count=request.data['count'],
        )
        new_dyson.save()

        return Response(data={'data': 'new dyson saved success'}, status=status.HTTP_201_CREATED)

    # def put(self, request, *args, **kwargs):


from rest_framework import serializers
from .models import DysonModel


class DysonSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False, default=None)

    class Meta:
        model = DysonModel
        fields = ['id', 'name', 'image', 'articul',
                  'price', 'country', 'characteristic',
                  'color', 'cap', 'count']


class DysonDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = DysonModel
        fields = ['name', 'image', 'articul',
                  'price', 'country', 'characteristic',
                  'color', 'cap', 'count']


class DysonUpdateDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = DysonModel
        fields = ['name', 'image', 'articul',
                  'price', 'country', 'characteristic',
                  'color', 'cap', 'count']

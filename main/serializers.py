from rest_framework import serializers
from .models import DysonModel


class DysonSerializer(serializers.ModelSerializer):

    class Meta:
        model = DysonModel
        fields = ('name', 'image', 'articul',
                  'price', 'country', 'characteristic',
                  'color', 'cap', 'count')
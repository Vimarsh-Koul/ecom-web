from rest_framework import serializers
from .models import category

class categoryserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = category
        fields = ('name','description')
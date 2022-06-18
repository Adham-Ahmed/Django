from unicodedata import name
from rest_framework import serializers
GENDER_LIST = [('male', 'male'), ('female', 'female')]

class ActorSerializer(serializers.Serializer):
    id= serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    gender = serializers.CharField(max_length=6,default='male')
    age = serializers.IntegerField(default=0)

from rest_framework import serializers
from actors.models import Actor


# from django.db.models.fields. import TextField
# from tags.models import Tag


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'
        # depth = 2



# class Tagserializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tag
#         fields = ['id']


# class JobCreateEditSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Job
#         fields = '__all__'

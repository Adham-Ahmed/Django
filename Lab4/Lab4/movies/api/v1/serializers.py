from rest_framework import serializers
from movies.models import Movie


# from django.db.models.fields. import TextField
# from tags.models import Tag


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
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

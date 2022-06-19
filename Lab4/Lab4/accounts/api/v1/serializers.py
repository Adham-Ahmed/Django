from webbrowser import get
from django.conf import settings
from rest_framework import serializers
from accounts.models import User
from django.contrib.auth import get_user_model


# User = get_user_model()
# settings.AUTH_USER_MODELuser=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
# from django.db.models.fields. import TextField
# from tags.models import Tag


#  Usage with models:


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['username', 'email', 'password','date_of_birth','avatar']
        # depth = 2



        extra_kwargs = {
            'password': {'write_only': True}
        }
        
    def create(self, validated_data):
        user = User(
            username=self.validated_data.get('username'),
            email=self.validated_data.get('email'),
            date_of_birth=self.validated_data.get('date_of_birth'),
            avatar=self.validated_data.get('avatar'),
        )
        user.set_password(validated_data['password'])
        user.save()

        return user
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
        
    # def save(self, **kwargs):
    #     user = User(
    #         username=self.validated_data.get('username')
    #     )
    #     user.save()

    #     return user
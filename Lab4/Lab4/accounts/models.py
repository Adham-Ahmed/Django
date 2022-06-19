from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.contrib.auth import get_user_model

# User = get_user_model()
# settings.AUTH_USER_MODELuser=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)


class User(AbstractUser):
        avatar = models.ImageField(verbose_name=('Avatar'), upload_to="avatar", null=True, blank=True)
        date_of_birth = models.DateField(auto_now_add=True, null=True, blank=True)



# settings.AUTH_USER_MODEL
# user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

from django.urls import path

from accounts.api.v1.view import index, detail, create, edit, delete
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('index/', index, name='index'),
    path('create/', create, name='create'),
    path('detail/<int:id>', detail, name='detail'),
    path('edit/<int:id>', edit, name='edit'),
    path('delete/<int:id>', delete, name='delete'),
    path('get-token/', obtain_auth_token)
]

from django.urls import path

from movies.api.v1.view import index, detail, create, edit, delete

urlpatterns = [
    path('index/', index, name='index'),
    path('create/', create, name='create'),
    path('detail/<int:id>', detail, name='detail'),
    path('edit/<int:id>', edit, name='edit'),
    path('delete/<int:id>', delete, name='delete'),
]

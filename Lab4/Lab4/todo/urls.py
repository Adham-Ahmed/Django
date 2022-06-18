from django.urls import path

from .views import *

app_name = 'todo'
urlpatterns = [
    path('home', home, name='home'),
    path('task/add', add_task, name='add'),
    path('task/<int:id>', detail, name='detail'),
    path('task/done/<int:id>', done, name='done'),
    path('task/delete/<int:id>', delete, name='delete')
]

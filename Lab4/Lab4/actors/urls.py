from django.contrib import admin
from django.urls import path

from .views import details_api, list_api, list_all_actors, delete_actor, add_actor, edit_actor,get_actor_details

app_name = 'actors'
urlpatterns = [
    path('list', list_all_actors, name='list'),
    path('add', add_actor, name='add'),
    path('edit/<int:id>', edit_actor, name='edit'),
    path('details/<int:id>', get_actor_details, name='details'),
    path('delete/<int:id>', delete_actor, name='delete'),
    path('list_api', list_api, name='list_api'),
    path('details_api/<int:id>', details_api, name='details_api'),

]

from django.urls import path

from .views import list_all_movies, delete_movie, add_movie, edit_movie,get_movie_details

app_name = 'movies'
urlpatterns = [
    path('list', list_all_movies, name='list'),
    path('add', add_movie, name='add'),
    path('edit/<int:id>', edit_movie, name='edit'),
    path('details/<int:id>', get_movie_details, name='details'),
    path('delete/<int:id>', delete_movie, name='delete'),

]

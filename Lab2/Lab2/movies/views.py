from django.shortcuts import render, redirect

from .forms import MovieForm

from .models import Movie


# Create your views here.
def list_all_movies(request):
    movies = Movie.objects.all()
    form = MovieForm()
    return render(request, 'movies/list.html', context={'movies': movies, 'form': form})


def add_movie(request):
    form = MovieForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('movies:list')


def edit_movie(request, **kwargs):
    id = kwargs['id']
    movie = Movie.objects.filter(id=id)[0]

    if request.method == 'GET':
        edit_form = MovieForm(instance=movie)
        return render(request, 'movies/edit.html', context={'form': edit_form, 'movie': movie})
    elif request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()

        return redirect('movies:list')


def delete_movie(request, **kwargs):
    id = kwargs['id']
    Movie.objects.filter(id=id).delete()
    return redirect('movies:list')


def get_movie_details(request, **kwargs):
    id = kwargs['id']
    record = Movie.objects.filter(id=id)[0]
    return render(request, 'movies/details.html', context={'movie': record})

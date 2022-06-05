from django.shortcuts import render, redirect

from .forms import ActorForm

from .models import Actor


# Create your views here.
def list_all_actors(request):
    actors = Actor.objects.all()
    form = ActorForm()
    return render(request, 'actors/list.html', context={'actors': actors, 'form': form})


def get_actor_details(request, **kwargs):
    id = kwargs['id']
    record = Actor.objects.filter(id=id)[0]
    return render(request, 'actors/details.html', context={'actor': record})


def add_actor(request):
    form = ActorForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('actors:list')


def edit_actor(request, **kwargs):
    id = kwargs['id']
    actor = Actor.objects.filter(id=id)[0]

    if request.method == 'GET':
        edit_form = ActorForm(instance=actor)
        return render(request, 'actors/edit.html', context={'form': edit_form, 'actor': actor})
    elif request.method == 'POST':
        form = ActorForm(request.POST, instance=actor)
        if form.is_valid():
            form.save()

        return redirect('actors:list')


def delete_actor(request, **kwargs):
    id = kwargs['id']
    Actor.objects.filter(id=id).delete()
    return redirect('actors:list')

from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import ActorForm
from .models import Actor
from .serializers import ActorSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404

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

    ###################################################
    ###################################################
    ###################################################


@api_view()
def list_api(request):
    actors = Actor.objects.all()
    serializer=ActorSerializer(actors,many=True)
    return Response(serializer.data)

@api_view()
def details_api(request,id):
    # print(kwargs)
    actor_id = id
    print(list(Actor.objects.all()))
    try:
        actor = Actor.objects.filter(id=actor_id).first()
        serializer=ActorSerializer(actor)
        return Response(serializer.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


    # actor_detail_api

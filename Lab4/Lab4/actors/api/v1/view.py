from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

# from Actors.api.v1.permissions import CompEditMyJopPermission, CompCreateActorPermission, DevApplyForActorPermission,DevCanApply
from actors.models import Actor
from actors.api.v1.serializers import ActorSerializer



@api_view(['GET'])
@permission_classes([])
def index(request):
    try:
        queryset = Actor.objects.all()
        serializer = ActorSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response({"status": "No Actors exist"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([])
def detail(request, id):
    response = {'data': {}, 'status': status.HTTP_404_NOT_FOUND}
    try:
        actor = Actor.objects.get(id=id)
        serializer = ActorSerializer(actor, many=False)
        response['data'] = serializer.data
        response['status'] = status.HTTP_200_OK
    except ObjectDoesNotExist:
        response['data'] = {'not found'}
        response['status'] = status.HTTP_204_NO_CONTENT
    except:
        response['data'] = {'server error'}
        response['status'] = status.HTTP_500_INTERNAL_SERVER_ERROR
    finally:
        return Response(**response)


@api_view(['POST'])
# @permission_classes([IsAuthenticated, CompCreateActorPermission])
def create(request):
    response = {'data': {}, 'status': status.HTTP_400_BAD_REQUEST}
    try:
        serializer = ActorSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            response['data'] = serializer.data
            response['status'] = status.HTTP_200_OK
        else:
            response['data'] = serializer.errors
    except:
        response['data'] = {'server error'}
        response['status'] = status.HTTP_500_INTERNAL_SERVER_ERROR
    finally:
        return Response(**response)


@api_view(['PUT', 'PATCH'])
# @permission_classes([IsAuthenticated, CompEditMyJopPermission])
def edit(request, Actor_id):
    response = {'data': {}, 'status': status.HTTP_400_BAD_REQUEST}
    try:
        Actor_instance = Actor.objects.get(id=Actor_id)

        if request.method == 'PUT':
            serializer = ActorSerializer(instance=Actor_instance, data=request.data)
        else:  # PATCH
            serializer = ActorSerializer(instance=Actor_instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            response['data'] = serializer.data
            response['status'] = status.HTTP_200_OK
        else:
            response['data'] = serializer.errors
    except:
        response['data'] = {'bad request'}
        response['status'] = status.HTTP_400_BAD_REQUEST
    finally:
        return Response(**response)


@api_view(['DELETE'])
# @permission_classes([IsAuthenticated, CompEditMyJopPermission])
def delete(request, actor_id):
    response = {'data': {}, 'status': status.HTTP_400_BAD_REQUEST}
    try:
        Actor.objects.get(id=actor_id).delete()
        response['data'] = {'deleted'}
        response['status'] = status.HTTP_204_NO_CONTENT
    except ObjectDoesNotExist:
        response['data'] = {'not found'}
        response['status'] = status.HTTP_404_NOT_FOUND
    finally:
        return Response(**response)
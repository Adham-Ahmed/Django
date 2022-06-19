from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

# from movies.api.v1.permissions import CompEditMyJopPermission, CompCreateMoviePermission, DevApplyForMoviePermission,DevCanApply
from movies.models import Movie
from movies.api.v1.serializers import MovieSerializer



@api_view(['GET'])
@permission_classes([])
def index(request):
    try:
        queryset = Movie.objects.all()
        serializer = MovieSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response({"status": "No Movies exist"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([])
def detail(request, id):
    response = {'data': {}, 'status': status.HTTP_404_NOT_FOUND}
    try:
        actor = Movie.objects.get(id=id)
        serializer = MovieSerializer(actor, many=False)
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
# @permission_classes([IsAuthenticated, CompCreateMoviePermission])
def create(request):
    response = {'data': {}, 'status': status.HTTP_400_BAD_REQUEST}
    try:
        serializer = MovieSerializer(data=request.data)
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
def edit(request, Movie_id):
    response = {'data': {}, 'status': status.HTTP_400_BAD_REQUEST}
    try:
        Movie_instance = Movie.objects.get(id=Movie_id)

        if request.method == 'PUT':
            serializer = MovieSerializer(instance=Movie_instance, data=request.data)
        else:  # PATCH
            serializer = MovieSerializer(instance=Movie_instance, data=request.data, partial=True)

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
        Movie.objects.get(id=actor_id).delete()
        response['data'] = {'deleted'}
        response['status'] = status.HTTP_204_NO_CONTENT
    except ObjectDoesNotExist:
        response['data'] = {'not found'}
        response['status'] = status.HTTP_404_NOT_FOUND
    finally:
        return Response(**response)
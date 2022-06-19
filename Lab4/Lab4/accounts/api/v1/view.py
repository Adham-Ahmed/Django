from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.authentication import TokenAuthentication 
from rest_framework.permissions import IsAuthenticated

# from Users.api.v1.permissions import CompEditMyJopPermission, CompCreateUserPermission, DevApplyForUserPermission,DevCanApply
from accounts.models import User
from accounts.api.v1.serializers import UserSerializer


@api_view(['GET'])
@permission_classes([])
def index(request):
    try:
        
        User=get_user_model()
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response({"status": "No Users exist"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([])
def detail(request, id):
    response = {'data': {}, 'status': status.HTTP_404_NOT_FOUND}
    try:
        User = User.objects.get(id=id)
        serializer = UserSerializer(User, many=False)
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
# @permission_classes([IsAuthenticated, CompCreateUserPermission])
def create(request):
    response = {'data': {}, 'status': status.HTTP_400_BAD_REQUEST}
    try:
        serializer = UserSerializer(data=request.data)
        # print(request.data.keys())
        # print(serializer)
        if serializer.is_valid():
            serializer.save()
            response['data'] = serializer.data
            response['status'] = status.HTTP_200_OK
        else:
            response['data'] = serializer.errors
    # except:
    #     response['data'] = {'server error'}
    #     response['status'] = status.HTTP_500_INTERNAL_SERVER_ERROR
    finally:
        return Response(**response)


@api_view(['PUT', 'PATCH'])
# @permission_classes([IsAuthenticated, CompEditMyJopPermission])
def edit(request, User_id):
    response = {'data': {}, 'status': status.HTTP_400_BAD_REQUEST}
    try:
        User_instance = User.objects.get(id=User_id)

        if request.method == 'PUT':
            serializer = UserSerializer(instance=User_instance, data=request.data)
        else:  # PATCH
            serializer = UserSerializer(instance=User_instance, data=request.data, partial=True)

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
def delete(request, User_id):
    response = {'data': {}, 'status': status.HTTP_400_BAD_REQUEST}
    try:
        User.objects.get(id=User_id).delete()
        response['data'] = {'deleted'}
        response['status'] = status.HTTP_204_NO_CONTENT
    except ObjectDoesNotExist:
        response['data'] = {'not found'}
        response['status'] = status.HTTP_404_NOT_FOUND
    finally:
        return Response(**response)
from .serializers import CustomUserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


@api_view(['POST'])
def create_user(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)
    if user:
        auth_token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': auth_token.key}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Wrong Credentials'}, status=status.HTTP_400_BAD_REQUEST)




@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    try:
        request.user.auth_token.delete()
        return Response({"message": "You are logged out."}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


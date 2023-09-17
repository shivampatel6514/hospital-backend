from django.shortcuts import render
from .serializers import CustomUserSerializer
from .models import CustomUser
# Create your views here.
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password  
from rest_framework.response import Response
from rest_framework import status,pagination

class CreateUserAPIView(APIView):

    # authentication_classes = [JWTTokenUserAuthentication]
    # permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()  # Create a copy of the request data
        password = data.pop('password', None)  # Remove the password from data and get it

        if password:
            data['password'] = make_password(password)  # Hash the password

        serializer = CustomUserSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "success": True,
                "message": "User Created successfully",
                "data": serializer.data,
            }, status=status.HTTP_201_CREATED)

        return Response({
            "success": False,
            "message": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

class DeleteUserAPIView(APIView):

    # authentication_classes = [JWTTokenUserAuthentication]
    # permission_classes = [IsAuthenticated]
    def delete(self, request, user_id):
        try:
            user = get_object_or_404(CustomUser, pk=user_id)  # Get the user instance by user_id
            user.delete()
            return Response({"success":True,"message": "User deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

        except CustomUser.DoesNotExist:
            return Response({"success":False,"message": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({"success":False,"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)    
        
class ListUserAPIView(APIView):
    # authentication_classes = [JWTTokenUserAuthentication]
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        custom_users = CustomUser.objects.all()
        serializer = CustomUserSerializer(custom_users, many=True)
        return Response({"success":True,"message":"data get successfully","data":serializer.data}, status=status.HTTP_200_OK)

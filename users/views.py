from django.shortcuts import render
from django.db.models import Q
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
# from users.serializers import RegisterSerializer
# from users.models import User



# class UserRegisterView(generics.GenericAPIView):
#     serializer_class = RegisterSerializer

#     def post(self, request):

#         data = request.data
#         print(data)
#         serializer = RegisterSerializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         user_data = serializer.data
#         username = serializer.data.get('username')
#         # tokens = User.objects.get(username=username).tokens
#         # user_data['tokens'] = tokens
#         return Response({"success": True, 'data': user_data}, status=status.HTTP_201_CREATED)
    

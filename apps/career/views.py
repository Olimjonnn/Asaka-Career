from django.shortcuts import render
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import generics
from apps.career.serializers import CareerSerializer, SuccesStoriesSerializer
from apps.career.models import Career, SuccessStories



class CareerView(generics.ListCreateAPIView):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request):
        career = Career.objects.last()
        ser = CareerSerializer(career)
        return Response(ser.data)
    
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':True, 'data': serializer.data}, status = 201)
        return Response({'status':False, 'data': serializer.errors}, status = 400)
    



class SuccessStoriesView(generics.ListAPIView):
    queryset = SuccessStories.objects.all().order_by('-id')[0:6]
    serializer_class = SuccesStoriesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    
    # Get function Succes Stories model!
    def list(self, request):
        succ = SuccessStories.objects.all()
        ser = SuccesStoriesSerializer(succ, many=True)
        return Response(ser.data)
    
    
    # Create function for Succes Stories model!
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':True, 'data': serializer.data}, status = 201)
        return Response({'status':False, 'data': serializer.errors}, status = 400)
    





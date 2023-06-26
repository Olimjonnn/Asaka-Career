from django.shortcuts import render
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import generics
from career.serializers import CareerSerializer, Succes_storiesSerializer
from career.models import Career, Success_stories



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
    



class Success_storiesView(generics.ListAPIView):
    queryset = Success_stories.objects.all().order_by('-id')[0:6]
    serializer_class = Succes_storiesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request):
        succ = Success_stories.objects.all()
        ser = Succes_storiesSerializer(succ, many=True)
        return Response(ser.data)
    
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':True, 'data': serializer.data}, status = 201)
        return Response({'status':False, 'data': serializer.errors}, status = 400)
    





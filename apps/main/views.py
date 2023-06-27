from django.shortcuts import render
from apps.main.serializers import SliderSerializer, CardTitlesSerializer, CardsSerializer, FooterSerializer
from apps.main.models import Slider, CardTitles, Cards, Footer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from apps.main.permissions import IsAdminOrReadOnly
from rest_framework import viewsets


class SliderView(generics.ListCreateAPIView, generics.DestroyAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    
    # Geting last object function for Slider model!
    def list(self, request):
        slider = self.queryset.last()
        return Response(self.serializer_class(slider).data)

    # Creating function for Slider model!
    def create(self, request, *args, **kwargs):
        serializier = SliderSerializer(data=request.data)
        if serializier.is_valid():
            serializier.save()
            return Response(serializier.data) 

    # Deleting function for Slider model! 
    def destroy(self, request, pk):
        slider = self.queryset.get(id=pk)
        slider.delete()
        return Response({"status": True, "message":"Deleted"})    



class CardsView(generics.RetrieveDestroyAPIView, generics.CreateAPIView):
    queryset = CardTitles.objects.all()
    serializer_class = CardTitlesSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    
    # Geting by id function for Cards Title model!
    def retrieve(self, request, pk, *args):
        card = CardTitles.objects.get(id=pk)
        serialializer = self.serializer_class(card).data
        return Response(serialializer)

    # Creating function for Cards Title model!
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
        
    # Deleting function for Cards Title model! 
    def destroy(self, request, pk):
        card = self.queryset.get(id=pk)
        card.delete()
        return Response({"status": True, "message" : "Deleted"})    


class SingleCart(generics.CreateAPIView, generics.DestroyAPIView):
    queryset = Cards.objects.all()
    serializer_class = CardsSerializer
    permission_classes = [IsAdminOrReadOnly]

    # Creating function for Cards model!
    def create(self, request):
        serializer = CardsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"status" : False, "message" : "Try again"})  
    
    # Deleting function for Cards model!
    def destroy(self, request, pk):
        card = self.queryset.get(id=pk)
        card.delete()
        return Response({"status": True, "message" : "Deleted"})   
    


class FooterView(generics.CreateAPIView):
    queryset = Footer.objects.all()
    serializer_class = FooterSerializer

    # Sending message function for Footer model!
    def create(self, request):
        serializer = FooterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"status" : False, "message" : "Try again"})    
    

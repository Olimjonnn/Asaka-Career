from django.shortcuts import render
from main.serializers import SliderSerializer, Card_TitlesSerializer, CardsSerializer, FooterSerializer
from main.models import Slider, Card_Titles, Cards, Footer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from main.permissions import IsAdminOrReadOnly
from rest_framework import viewsets


class SliderView(generics.ListCreateAPIView, generics.DestroyAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    

    def list(self, request):
        slider = self.queryset.last()
        return Response(self.serializer_class(slider).data)


    def create(self, request, *args, **kwargs):
        serializier = SliderSerializer(data=request.data)
        if serializier.is_valid():
            serializier.save()
            return Response(serializier.data) 

    def destroy(self, request, pk):
        slider = self.queryset.get(id=pk)
        slider.delete()
        return Response({"status": True, "message":"Deleted"})    



class CardsView(generics.RetrieveDestroyAPIView, generics.CreateAPIView):
    queryset = Card_Titles.objects.all()
    serializer_class = Card_TitlesSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    
    def retrieve(self, request, pk, *args):
        card = Card_Titles.objects.get(id=pk)
        serialializer = self.serializer_class(card).data
        return Response(serialializer)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
        

    def destroy(self, request, pk):
        card = self.queryset.get(id=pk)
        card.delete()
        return Response({"status": True, "message" : "Deleted"})    


class SingleCart(generics.CreateAPIView, generics.DestroyAPIView):
    queryset = Cards.objects.all()
    serializer_class = CardsSerializer
    permission_classes = [IsAdminOrReadOnly]


    def create(self, request):
        serializer = CardsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"status" : False, "message" : "Try again"})  
    

    def destroy(self, request, pk):
        card = self.queryset.get(id=pk)
        card.delete()
        return Response({"status": True, "message" : "Deleted"})   
    


class FooterView(generics.CreateAPIView):
    queryset = Footer.objects.all()
    serializer_class = FooterSerializer

    def create(self, request):
        serializer = FooterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"status" : False, "message" : "Try again"})    
    

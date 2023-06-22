from django.shortcuts import render
from vacancy.models import Hashtags,Apply, Vacancy, Requirements, Responsibilities, Conditions, Location
from vacancy.serializers import VacancyDetailSerializers, HashtagsSerializer, ApplySerializer, VacancySerializer, RequirementsSerializer, ResponsibilitiesSerializer, ConditionsSerializer, LocationSerializer
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response

class HashtagsView(generics.CreateAPIView):
    queryset = Hashtags.objects.all()
    serializer_class = HashtagsSerializer
    permission_classes = [permissions.IsAuthenticated]



class RequirementsView(generics.CreateAPIView):
    queryset = Requirements.objects.all()
    serializer_class = RequirementsSerializer
    permission_classes = [permissions.IsAuthenticated]



class ResponsibilitiesView(generics.CreateAPIView):
    queryset = Responsibilities.objects.all()
    serializer_class = ResponsibilitiesSerializer
    permission_classes = [permissions.IsAuthenticated]



class ConditionsView(generics.CreateAPIView):
    queryset = Conditions.objects.all()
    serializer_class = HashtagsSerializer
    permission_classes = [permissions.IsAuthenticated]



class LocationView(generics.CreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [permissions.IsAuthenticated]


class ApplyView(generics.CreateAPIView):
    queryset = Apply.objects.all()
    serializer_class = ApplySerializer
    
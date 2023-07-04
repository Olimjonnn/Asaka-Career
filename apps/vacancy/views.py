from django.shortcuts import render
from apps.vacancy.models import Apply, Vacancy, Requirements, Responsibilities, Conditions, Location
from apps.vacancy.serializers import VacancyDetailSerializers,  ApplySerializer, VacancySerializer, RequirementsSerializer, ResponsibilitiesSerializer, ConditionsSerializer, LocationSerializer
from rest_framework import generics, status
from rest_framework import permissions
from rest_framework.response import Response
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend




class RequirementsView(generics.CreateAPIView):
    queryset = Requirements.objects.all()
    serializer_class = RequirementsSerializer
    permission_classes = [permissions.IsAuthenticated]
    # Creating function for Requirements model!


class ResponsibilitiesView(generics.CreateAPIView):
    queryset = Responsibilities.objects.all()
    serializer_class = ResponsibilitiesSerializer
    permission_classes = [permissions.IsAuthenticated]
    # Creating function for Responsibilities model!



class ConditionsView(generics.CreateAPIView):
    queryset = Conditions.objects.all()
    serializer_class = ConditionsSerializer
    permission_classes = [permissions.IsAuthenticated]
    # Creating function for Conditions model!



class LocationView(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [permissions.IsAuthenticated]
    # Creating and Geting function for Location model!


class ApplyView(generics.ListCreateAPIView):
    queryset = Apply.objects.all()
    serializer_class = ApplySerializer
    # Applying function for Apply model!

class VacancyView(generics.ListCreateAPIView, generics.UpdateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyDetailSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Function: Creating with nested serializer for Vacancy model!
    def create(self, request, *args, **kwargs):
        if request.user.is_staff:
            request.data['added_by'] = request.user.id
            request.data['modified_by'] = request.user.id
            return super().create(request, *args, **kwargs)

        return Response({'detail': 'You do not have permission to perform this action.'},
                        status=status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        if request.user.is_staff:
            request.data['modified_by'] = request.user.id
            return super().update(request, *args, **kwargs)
        return Response({'detail': 'You do not have permission to perform this action.'},
                        status=status.HTTP_403_FORBIDDEN)

    

    # Function: Filtering by few fields for Vacancy model!
    def get_queryset(self):
        vacancy = super().get_queryset()
        filter_field = self.request.GET.get("filter_field")
        filtering = Q()
        if filter_field:
            filtering = Q(category__name__icontains=filter_field) | Q(title__icontains=filter_field) | Q(city__icontains=filter_field) |  Q(worker_experience__icontains=filter_field)
        queryset = vacancy.filter(filtering)
        print(queryset)
        return queryset
    
    # Function: Getting by few fields for Vacancy model!   
    def list(self, request, *args, **kwargs):
            queryset = self.get_queryset()
            if queryset:
                serializer = self.serializer_class(queryset, many=True).data
                count = queryset.count()
                return Response({'success': True, 'count':count, 'data': serializer}, status=200)
            return Response({'success': False, 'data': "Vacancy matching query does not exist"}, status=404)


class RelatedVacancy(generics.RetrieveAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyDetailSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Function: Getting Related objects by category, for Vacancy model!   
    def retrieve(self, request, pk):
        vacancy = Vacancy.objects.get(id=pk)
        ser_vac = self.get_serializer(vacancy).data
        related = Vacancy.objects.filter(category__id=vacancy.category.id)[0:2]
        ser_rel = self.get_serializer(related, many=True).data
        return Response({"status":True, "Vacancy":ser_vac, "Related vacancies":ser_rel})
    

class ApplyingView(generics.ListCreateAPIView):
    queryset = Apply.objects.all()
    serializer_class = ApplySerializer

    # Sending applyment function for Apply model!
    def create(self, request, pk):
        vacancy_id = Vacancy.objects.get(id=pk)
        if vacancy_id:
            ser = self.serializer_class(data=request.data)
            if ser.is_valid():
                ser.save()
                return Response(ser.data)
            return Response({"status":False, "error":ser.errors})
        return Response({"Vacancy matching query does not exist"})
        

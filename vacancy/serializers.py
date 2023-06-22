from rest_framework import serializers
from vacancy.models import Hashtags,Apply, Vacancy, Requirements, Responsibilities, Conditions, Location


class HashtagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtags
        fields = '__all__'


class RequirementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirements
        fields = '__all__'


class ResponsibilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsibilities
        fields = '__all__'


class ConditionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conditions
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class VacancySerializer(serializers.ModelSerializer):

    class Meta:
        model = Vacancy
        fields = [
            'id',
            'title',
            'rates',
            'city',
            'text',
            'hashtags',
        ]


class VacancyDetailSerializers(serializers.ModelSerializer):
    vacancy_requirements = RequirementsSerializer(many=True)
    vacancy_responsibilities = ResponsibilitiesSerializer(many=True)
    vacancy_conditions = ConditionsSerializer(many=True)
    vacancy_location = LocationSerializer(many=True)

    class Meta:
        model = Vacancy
        fields = [
            'id',
            'title',
            'rates',
            'working_days',
            'worker_level',
            'vacancy_requirements',
            'vacancy_responsibilities',
            'vacancy_conditions',
            'vacancy_location'
            'hashtags',
        ]

class ApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Apply
        fields = '__all__'

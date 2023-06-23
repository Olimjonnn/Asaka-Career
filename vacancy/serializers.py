from rest_framework import serializers
from vacancy.models import Hashtags,Apply, Vacancy, Requirements, Responsibilities, Conditions, Location, Category


class HashtagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtags
        fields = '__all__'
        read_only_fields = ('vacancy_hashtags', )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class RequirementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirements
        fields = '__all__'
        read_only_fields = ('vacancy', )


class ResponsibilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsibilities
        fields = '__all__'
        read_only_fields = ('vacancy', )

class ConditionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conditions
        fields = '__all__'
        read_only_fields = ('vacancy', )

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
        read_only_fields = ('vacancy', )

class VacancySerializer(serializers.ModelSerializer):
    vacancy_hashtags = HashtagsSerializer(many=True, read_only=True)
    class Meta:
        model = Vacancy
        fields = [
            'id',
            'title',
            'rates',
            'city',
            'text',
            'vacancy_hashtags'
        ]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class VacancyDetailSerializers(serializers.ModelSerializer):
    vacancy_requirements = RequirementsSerializer(many=True)
    vacancy_responsibilities = ResponsibilitiesSerializer(many=True)
    vacancy_conditions = ConditionsSerializer(many=True)
    vacancy_location = LocationSerializer(many=True)
    vacancy_hashtags = HashtagsSerializer(many=True)
    class Meta:
        model = Vacancy
        fields = [
            'id',
            'title',
            'text',
            'rates',
            'city',
            'category',
            'working_days',
            'worker_level',
            'worker_experience',
            'vacancy_requirements',
            'vacancy_responsibilities',
            'vacancy_conditions',
            'vacancy_location',
            'vacancy_hashtags'
        ]
    def create(self, validated_data):
        vacancy_requirements = validated_data.pop('vacancy_requirements')
        vacancy_responsibilities = validated_data.pop('vacancy_responsibilities')
        vacancy_conditions = validated_data.pop('vacancy_conditions')
        vacancy_location = validated_data.pop('vacancy_location')
        vacancy_hashtags = validated_data.pop('vacancy_hashtags')
        vacancy_instance = Vacancy.objects.create(**validated_data)

        for requirement in vacancy_requirements:
            Requirements.objects.create(vacancy=vacancy_instance, **requirement) 
        
        for responsibility in vacancy_responsibilities:
            Responsibilities.objects.create(vacancy=vacancy_instance, **responsibility)  
                  
        for condition in vacancy_conditions:
            Conditions.objects.create(vacancy=vacancy_instance, **condition)      

        for location in vacancy_location:
            Location.objects.create(vacancy=vacancy_instance, **location)  

        for hashtag in vacancy_hashtags:
            Hashtags.objects.create(vacancy_hashtags=vacancy_instance, **hashtag) 
        
        return vacancy_instance

class ApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Apply
        fields = '__all__'

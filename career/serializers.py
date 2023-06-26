from rest_framework import serializers
from career.models import Career, Success_stories



class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = '__all__'

    def create(self, validated_data):
        return Career.objects.create(**validated_data)

class Succes_storiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Success_stories
        fields = ['id', 'title', 'text', 'image']
    
    def create(self, validated_data):
        return Career.objects.create(**validated_data)
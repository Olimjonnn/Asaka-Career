from rest_framework import serializers
from apps.career.models import Career, SuccessStories



class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = '__all__'

    def create(self, validated_data):
        return Career.objects.create(**validated_data)

class SuccesStoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuccessStories
        fields = ['id', 'title', 'text', 'image']
    
    def create(self, validated_data):
        return Career.objects.create(**validated_data)
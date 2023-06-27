from rest_framework import serializers
from apps.blog.models import Blog



class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'text', 'image']




class BlogDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = [
            'id',
            'title',
            'text',
            'image',
            'created_date',
            'views',
            'title2',
            'text2',
            'image2',
            'title3',
            'text3',
            'image3',
        ]

    def create(self, validated_data):
        return Blog.objects.create(**validated_data)


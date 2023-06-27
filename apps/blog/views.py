from django.shortcuts import render
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import generics
from apps.blog.serializers import BlogSerializer, BlogDetailSerializer
from apps.blog.models import Blog


class BlogView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogDetailView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Get function for Blog model!
    def list(self, request, pk):
        queryset = Blog.objects.all().filter(id=pk) 
        for i in queryset:
            i.views += 1
            i.save()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    
    # Create function for Blog model!
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':True, 'data': serializer.data}, status = 201)
        return Response({'status':False, 'data': serializer.errors}, status = 400)
    


class RecomendedBlogs(generics.ListAPIView):
    queryset = Blog.objects.all().order_by('-id')[0:6]
    serializer_class = BlogSerializer


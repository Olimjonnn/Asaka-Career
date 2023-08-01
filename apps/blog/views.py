from django.shortcuts import render
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import generics
from apps.blog.serializers import BlogSerializer, BlogDetailSerializer
from apps.blog.models import Blog

from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from apps.blog.scrape import scrape_news


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
    


@api_view(['POST'])
@permission_classes([AllowAny])
def capturing_screenshot(request):
    url = request.data.get('url')

    options = webdriver.ChromeOptions()
    service = Service(executable_path='./chromedriver.exe')
    options.add_argument('--headless') 
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(url)
        screenshot_path = '/path/to/save/screenshot.png'
        driver.save_screenshot(screenshot_path)
        driver.quit()
        return JsonResponse({'message': 'Screenshot captured successfully.', 'screenshot_path': screenshot_path})
    except Exception as e:
        return JsonResponse({'error': str(e)})

    
def get_news(request):
    news_data = scrape_news()
    return JsonResponse(news_data, safe=False)

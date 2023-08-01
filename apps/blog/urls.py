from django.urls import path
from apps.blog.views import BlogView, BlogDetailView, capturing_screenshot, get_news

urlpatterns = [
    path('blog/blogs/', BlogView.as_view()),
    path('blog/blog-detail/<int:pk>', BlogDetailView.as_view()),
    path('capturing-screenshot/', capturing_screenshot, name='capturing-screenshot'),
    path('get_news/', get_news, name='get_news'),
]


from django.urls import path
from apps.blog.views import BlogView, BlogDetailView, RecomendedBlogs

urlpatterns = [
    path('blog/blogs/', BlogView.as_view()),
    path('blog/blog-detail/<int:pk>', BlogDetailView.as_view()),
    path('blog/recomended-blogs/', RecomendedBlogs.as_view()),
]


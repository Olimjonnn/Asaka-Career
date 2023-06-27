from django.urls import path
from apps.career.views import *


urlpatterns = [
    path('career/career/', CareerView.as_view()),
    path('career/success-stories/', SuccessStoriesView.as_view()),
]

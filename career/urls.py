from django.urls import path
from career.views import *


urlpatterns = [
    path('career/career/', CareerView.as_view()),
    path('career/success-stories/', Success_storiesView.as_view()),
]

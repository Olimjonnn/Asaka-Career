from django.urls import path
from vacancy.views import ApplyView

urlpatterns = [
    path('vacancy/create/', ApplyView.as_view())
]

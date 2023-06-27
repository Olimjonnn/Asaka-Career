from django.urls import path
from apps.vacancy.views import ApplyView, VacancyView, RelatedVacancy, ApplyingView

urlpatterns = [
    path('vacancy/create/', ApplyView.as_view()),
    path('vacancy/vacancy/', VacancyView.as_view()),
    path('vacancy/relatedvacancy/<int:pk>', RelatedVacancy.as_view()),
    path('vacancy/applying/<int:pk>', ApplyingView.as_view()),
    
]

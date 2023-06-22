from django.urls import path
from main.views import SliderView, CardsView, FooterView


urlpatterns = [
    path("main/sliders/", SliderView.as_view()),
    path("main/sliders/<int:pk>", SliderView.as_view()),
    path("main/cards/<int:pk>", CardsView.as_view()),
    path("main/cards/", CardsView.as_view()),
    path("main/footer/", FooterView.as_view()),
]


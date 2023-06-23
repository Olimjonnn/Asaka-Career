from django.urls import path, include
from main.views import SliderView, CardsView, FooterView, SingleCart




urlpatterns = [
    path("main/sliders/", SliderView.as_view()),
    path("main/sliders/<int:pk>", SliderView.as_view()),
    path("main/cards/<int:pk>", CardsView.as_view()),
    path("main/cards/", CardsView.as_view()),
    path("main/footer/", FooterView.as_view()),
    path("main/singlecard/", SingleCart.as_view()),
]


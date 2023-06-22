from django.db import models
from phone_field import PhoneField


class Slider(models.Model):
    title = models.CharField(max_length=55, verbose_name="slider_title")
    text = models.CharField(max_length=255, verbose_name='slider_video')
    file = models.FileField(upload_to='media/')

    def __str__(self) -> str:
        return self.title


class Card_Titles(models.Model):
    title = models.CharField(max_length=55)
    title2 = models.CharField(max_length=255, null=True, blank=True, verbose_name='card_title2')
    
    def __str__(self) -> str:
        return self.title

    @property
    def cards_title(self):
        return self.cards_title_set.all()


class Cards(models.Model):
    title = models.CharField(max_length=32, verbose_name="cards_title")
    icon = models.ImageField(upload_to='media/', blank=True, null=True)
    card_title = models.ForeignKey(Card_Titles, on_delete=models.CASCADE, related_name="cards_title")
   
    def __str__(self) -> str:
        return self.title

class Footer(models.Model):
    phone = PhoneField(help_text='Contact phone number')
    letter = models.TextField()

    def __str__(self) -> str:
        return self.phone
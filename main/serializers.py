from rest_framework import serializers
from main.models import Slider, Card_Titles, Cards, Footer

class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ['id', 'title', 'text', 'file']

    def create(self, validated_data):
        return Slider.objects.create(**validated_data)


class CardsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cards
        fields = ['id', 'title', 'icon', 'card_title']
        read_only_fields = ('card_title', )


    def create(self, validated_data):
        return Cards.objects.create(**validated_data)

    

class Card_TitlesSerializer(serializers.ModelSerializer):
    cards_title = CardsSerializer(many=True)
    class Meta:
        model = Card_Titles
        fields = ['id', 'title', 'title2', 'cards_title']


    def create(self, validated_data):
        cards_title = validated_data.pop('cards_title')
        print(cards_title)
        card_title = super().create(**validated_data)
        print(card_title)
        for cards in cards_title:
            Cards.objects.create(cards, card_title=card_title)
        return card_title


class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = ['id', 'phone', 'letter']

    def create(self, validated_data):
        return Footer.objects.create(**validated_data)

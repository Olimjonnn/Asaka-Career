from rest_framework import serializers
from apps.main.models import Slider, CardTitles, Cards, Footer

class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ['id', 'title', 'text', 'file']

    def create(self, validated_data):
        return Slider.objects.create(**validated_data)


class CardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cards
        fields = ['id', 'title', 'card_title']
        read_only_fields = ('card_title', )


    def create(self, validated_data):
        return Cards.objects.create(**validated_data)

    

class CardTitlesSerializer(serializers.ModelSerializer):
    card_title = CardsSerializer(many=True)
    class Meta:
        model = CardTitles
        fields = "__all__"


    def create(self, validated_data):
        card_title = validated_data.pop('card_title')
        card_instance = CardTitles.objects.create(**validated_data)
        for card in card_title:
            Cards.objects.create(card_title=card_instance, **card)
        return card_instance




class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = ['id', 'phone', 'letter']

    def create(self, validated_data):
        return Footer.objects.create(**validated_data)

from rest_framework import serializers
from apps.main.models import Slider, CardTitles, Cards, Footer

class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ['id', 'title', 'text', 'file']

    def create(self, validated_data):
        return Slider.objects.create(**validated_data)


class CardsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Cards
        fields = ['id', 'title', 'card_title']
        read_only_fields = ('card_title', 'id')


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

    def update(self, instance, validated_data):
        card_title_data = validated_data.pop('card_title')
        cards = (instance.card_title).all()
        cards = list(cards)
        instance.title = validated_data.get("title", instance.title)
        instance.save()
        
        for i in card_title_data:
            print(list(i.keys()))
            if "id" in i.keys():
                card = cards.pop(0)
                card.title = i.get('title', card.title)
                card.save()
            else:
                c = Cards.objects.update_or_create(**i, card_title=instance)
                
        return instance

class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = ['id', 'phone', 'letter']

    def create(self, validated_data):
        return Footer.objects.create(**validated_data)

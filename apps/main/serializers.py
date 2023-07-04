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

    def update(self, instance, validated_data):
        card_title_data = validated_data.pop('card_title')
        instance.title = validated_data.get("title", instance.title)
        instance.save()
        for i in card_title_data:
            card = Cards.objects.get(pk=i['id'])
            card.title = i.get('title', card.title)
            card.save()

        # keep_cards = []
        # # existing_ids = [c.id for c in instance.card_title]
        # for i in card_title:
        #     if "id" in i.keys():
        #         if Cards.objects.filter(id=i['id']).exists():
        #             c = Cards.objects.get(id=i['id'])
        #             c.title = i.get('title', c.title)
        #             c.save()
        #             keep_cards.append(c)
        #         else:
        #             continue
        #     else:
        #         c = Cards.objects.create(**i, card_title=instance)
        #         keep_cards.append(c)

        # # for i in instance.card_title:
        # #     if i.id not in keep_cards:
        # #         i.delete()
        return instance

class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = ['id', 'phone', 'letter']

    def create(self, validated_data):
        return Footer.objects.create(**validated_data)

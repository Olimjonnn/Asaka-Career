# Generated by Django 4.2.2 on 2023-06-26 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_cards_card_title'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Card_Titles',
            new_name='CardTitles',
        ),
    ]
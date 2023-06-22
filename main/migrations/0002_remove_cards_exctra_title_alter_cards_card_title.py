# Generated by Django 4.2.2 on 2023-06-22 04:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cards',
            name='exctra_title',
        ),
        migrations.AlterField(
            model_name='cards',
            name='card_title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards_title', to='main.card_titles'),
        ),
    ]
# Generated by Django 4.2.2 on 2023-06-22 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_card_titles_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cards',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]

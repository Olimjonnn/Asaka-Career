# Generated by Django 4.2.2 on 2023-06-22 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0003_vacancy_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vacancy',
            old_name='hashtag',
            new_name='hashtags',
        ),
    ]

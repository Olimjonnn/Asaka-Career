# Generated by Django 4.2.2 on 2023-06-22 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0002_vacancy_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='text',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.2.2 on 2023-06-27 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0002_rename_success_histories_success_stories'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Success_stories',
            new_name='SuccessStories',
        ),
    ]

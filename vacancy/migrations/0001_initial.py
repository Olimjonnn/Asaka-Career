# Generated by Django 4.2.2 on 2023-06-22 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hashtag', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='vacancy_title')),
                ('rates', models.IntegerField(choices=[(0, '0.25'), (1, 'Half time'), (2, '0.75'), (3, 'Full time')], default=3)),
                ('working_days', models.CharField(max_length=100, verbose_name='vacancy_working_days')),
                ('worker_level', models.IntegerField(choices=[(0, 'Junior'), (1, 'Middle'), (2, 'Senior')], default=2)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('hashtag', models.ManyToManyField(to='vacancy.hashtags')),
            ],
        ),
        migrations.CreateModel(
            name='Responsibilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancy_responsibilities', to='vacancy.vacancy')),
            ],
        ),
        migrations.CreateModel(
            name='Requirements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancy_requirements', to='vacancy.vacancy')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.CharField(max_length=40)),
                ('longitude', models.CharField(max_length=40)),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancy_location', to='vacancy.vacancy')),
            ],
        ),
        migrations.CreateModel(
            name='Conditions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancy_conditions', to='vacancy.vacancy')),
            ],
        ),
    ]
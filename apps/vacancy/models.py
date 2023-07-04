from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import User
from users.models import User
from apps.vacancy.constants import JOB_TYPE, CANDIDATE_LEVEL

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self) -> str:
        return self.name
    

class Vacancy(models.Model):

    title = models.CharField(max_length=255, verbose_name='vacancy_title')
    job_type = models.CharField(max_length=20, choices=JOB_TYPE.CHOICES)
    candidate_level = models.CharField(max_length=50, choices=CANDIDATE_LEVEL.CHOICES)
    text = models.TextField()
    working_days = models.CharField(max_length=100, verbose_name='vacancy_working_days')
    added_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    city = models.CharField(max_length=40)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    worker_experience = models.IntegerField()
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='added_by')
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                    related_name='modified_by')

    tags = models.ManyToManyField(Tag, related_name='vacancies', blank=True)

    def __str__(self) -> str:
        return self.title 






class Requirements(models.Model):
    text = models.CharField(max_length=100)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='vacancy_requirements')

    def __str__(self) -> str:
        return self.text 


class Responsibilities(models.Model):
    text = models.CharField(max_length=100)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='vacancy_responsibilities')

    def __str__(self) -> str:
        return self.text 


class Conditions(models.Model):
    text = models.CharField(max_length=100)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='vacancy_conditions')

    def __str__(self) -> str:
        return self.text 


class Location(models.Model):
    latitude = models.CharField(max_length=40)
    longitude = models.CharField(max_length=40)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='vacancy_location')


class Apply(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.IntegerField(help_text='Contact phone number')
    cv = models.FileField(upload_to='media/', null=True)
    def __str__(self):
        return self.name



from django.db import models
from phone_field import PhoneField


class Hashtags(models.Model):
    hashtag = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.hashtag

class Category(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self) -> str:
        return self.name
    

class Vacancy(models.Model):
    RATES = (
        (0, "0.25"),
        (1, "Half time"),
        (2, "0.75"),
        (3, "Full time"),
    )
    WORKER_LEVEL = (
        (0, 'Junior'),
        (1, 'Middle'),
        (2, 'Senior')
    )
    title = models.CharField(max_length=255, verbose_name='vacancy_title')
    rates = models.IntegerField(choices=RATES, default=3)
    text = models.TextField()
    working_days = models.CharField(max_length=100, verbose_name='vacancy_working_days')
    worker_level = models.IntegerField(choices=WORKER_LEVEL, default=2)
    created_date = models.DateTimeField(auto_now_add=True)
    city = models.CharField(max_length=40)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    worker_experience = models.IntegerField()


    def __str__(self) -> str:
        return self.title 


class Hashtags(models.Model):
    hashtag = models.CharField(max_length=40)
    vacancy_hashtags = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='vacancy_hashtags')
    def __str__(self) -> str:
        return self.hashtag



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



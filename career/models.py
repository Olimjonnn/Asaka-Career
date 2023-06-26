from django.db import models



class Career(models.Model):
    image = models.ImageField(upload_to='media/')
    employers = models.IntegerField()
    youngers = models.FloatField()
    higher_education = models.IntegerField()
    specialist_in_banking = models.IntegerField()


class Success_stories(models.Model):
    title = models.CharField(max_length=80, verbose_name='Title')
    text = models.TextField(verbose_name='Text')
    image = models.ImageField(upload_to='media/')





from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=80, verbose_name='Blog_Title')
    text = models.TextField(verbose_name='Blog_Text')
    image = models.ImageField(upload_to='media/')
    created_date = models.DateField(auto_now_add=True)
    views = models.IntegerField(default=1)
    
    # Blog Detail informations

    title2 = models.CharField(max_length=80, verbose_name='Blog_Title1', null=True)
    text2 = models.TextField(verbose_name='Blog_Text2', null=True)
    image2 = models.ImageField(upload_to='media/', null=True)

    title3 = models.CharField(max_length=80, verbose_name='Blog_Title3', null=True)
    text3 = models.TextField(verbose_name='Blog_Text3', null=True)
    image3 = models.ImageField(upload_to='media/', null=True)

    def __str__(self) -> str:
        return self.title
    

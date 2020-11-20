from django.db import models
from django.urls import reverse

# Create your models here.
class school(models.Model):
    name=models.CharField(max_length=264)
    principal=models.CharField(max_length=264)
    location=models.CharField(max_length=264)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('my_app:detail',kwargs={'pk':self.pk})

class students(models.Model):
    name=models.CharField(max_length=264)
    age=models.PositiveIntegerField()
    school=models.ForeignKey(school,on_delete=models.CASCADE,related_name='students')

    def __str__(self):
        return self.name

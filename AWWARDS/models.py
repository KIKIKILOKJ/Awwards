from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.

class Profile(models.Model):
    profile_picture=models.ImageField(upload_to = 'images/')
    bio=models.CharField(max_length=100)
    contact=models.CharField(max_length=50)
    user=models.OneToOneField(User,null=True)
    pub_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

class Projects(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to = 'images')
    description = models.CharField(max_length=300)
    link = models.CharField(max_length=100)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete

class RateReview(models.Model):#
    design=models.PositiveIntegerField(validators=[MinValueValidator(0),MaxValueValidator(10)])
    usability = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    content = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])

    def save_ratereview(self):
        self.save()

    @classmethod
    def search_project(cls,title):
        project = cls.objects.filter(title__icontains=title)
        return project

from django.db import models

# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to = 'images')
    description = models.CharField(max_length=300)
    link = models.CharField(max_length=100)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    
class Profile(models.Model):
    profile_picture=models.ImageField(upload_to = 'images/')
    bio=models.CharField(max_length=100)
    contact=models.CharField(max_length=50)
    user=models.OneToOneField(User,null=True)
    pub_date=models.DateTimeField(auto_now_add=True)
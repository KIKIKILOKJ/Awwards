from django.db import models

# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to = 'ards/',default='Project Image')
    description = models.CharField(max_length=300)
    link = models.CharField(max_length=100)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
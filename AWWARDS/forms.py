from django import forms
from .models import Project

class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user', 'pub_date', 'profile']
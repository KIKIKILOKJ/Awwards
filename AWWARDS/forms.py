from django import forms
from .models import Projects,Profile

class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Projects
        exclude = ['user', 'pub_date', 'profile']
        
class EditProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['user', 'pub_date', 'profile']
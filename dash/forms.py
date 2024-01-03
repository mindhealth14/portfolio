from django import forms
from myport.models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['category', 'title', 'description', 'slug', 'image', 'image_url', 'embed_code', 'git_source_code']

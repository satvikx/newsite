from django import forms
from django.forms import ModelForm
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'points', 'description','due_date', 'users')
        labels = {
			'name': '',
			'points': '',
			'description': '',
			'due-date': '',
			'users': 'Select User',			
		}
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Project Name'}),
            'points': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Points'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter a Description'}),
            'due_date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'Deadline', 'class': 'form-control'}),		
            #'users': forms.Select(attrs={'class':'form-control', 'placeholder':'User'}),
        }


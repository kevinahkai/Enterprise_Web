from dataclasses import field
from django import forms
from .models import Conference, Project

class ConferenceForm(forms.ModelForm):
    class Meta:
        model = Conference
        fields = ['title', 'host', 'convenor', 'issue', 'date', 'place', 'content', 'file', 'project']
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
            'host' : forms.TextInput(attrs={'class' : 'form-control'}),
            'convenor' : forms.TextInput(attrs={'class' : 'form-control'}),
            'issue' : forms.TextInput(attrs={'class' : 'form-control'}),
            'date' : forms.DateInput(attrs={'class' : 'form-control'}),
            'place' : forms.TextInput(attrs={'class' : 'form-control'}),
            'content' : forms.Textarea(attrs={'class' : 'form-control'}),
        }

        labels = {
            'title' : '會議名稱',
            'host' : '主席',
            'convenor' : '主辦單位',
            'issue' : '議題',
            'date' : '會議日期',
            'place' : '會議地點',
            'content' : '內容',
        }
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'start_date', 'exp_date', 'end_date', 'intro', 'principal']
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'start_date' : forms.DateInput(attrs={'type' : 'hidden'}),
            'exp_date' : forms.TextInput(attrs={'class' : 'form-control'}),
            'end_date' : forms.TextInput(attrs={'class' : 'form-control'}),
            'intro' : forms.Textarea(attrs={'class' : 'form-control'}),
        }

        labels = {
            'name' : '專案名稱',
            'intro' : '專案介紹',
            'start_date' : '開始日',
            'exp_date' : '預期結束日',
            'end_date' : '結束日',
        }
    

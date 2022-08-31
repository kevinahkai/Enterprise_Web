from urllib import request
from django import forms
from .models import News
import datetime

class NewsForm(forms.ModelForm):
    
    class Meta:
        model = News
        fields = ['title', 'content', 'Date', 'file']
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
            'content' : forms.Textarea(attrs={'class' : 'form-control'}), 
            'Date' : forms.DateInput(attrs={'type' : 'hidden'}),
            #'file' : forms.FileInput(attrs={'blank' : 'True'}),
        }

        labels = {
            'title' : '標題',
            'content' : '內容',
            'file' : '附加檔案',
        }
#公告
from curses.ascii import US
from django.db import models
from django.contrib.auth.models import User
from members.models import Account

class Topic(models.Model):
    text=models.CharField(max_length=100)
    date_added=models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey(Account,on_delete=models.CASCADE)
    def __str__(self):
        return self.text

class Entry(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'entries'
 
    def __str__(self):
        return self.text

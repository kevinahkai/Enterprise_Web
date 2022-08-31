import imp
from django.db import models
from django.utils import timezone
from members.models import Account

class News(models.Model):
    title = models.CharField(max_length=100, null=False)
    content = models.TextField(null=False)
    Date = models.DateField(default=timezone.now, null=False)
    Last_modify = models.DateField(auto_now=True, null=False)   #auto_now，每次修改，時間都會更新
    department = models.CharField(max_length=30, null=False, default="未設置")
    owner=models.ForeignKey(Account,on_delete=models.CASCADE, default=True)
    file = models.FileField(upload_to='uploads/', blank=True, null=True)

    class Meta:
        permissions = [
            ("can_read", "Can read"),
            ("can_insert", "Can add announce"),
            ("can_update", "Can edit announce"),
            ("can_delete", "Can delete announce"),
        ]

    def __str__(self):
        return self.title


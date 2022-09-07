from django.db import models
from django.utils import timezone
from members.models import Account

class Project(models.Model):
    name = models.CharField(max_length=100, null=False)
    intro = models.TextField(null=False)
    start_date = models.DateField(default=timezone.now, null=False)
    exp_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    principal = models.ForeignKey(Account, on_delete=models.CASCADE)

    class Meta:
        permissions = []

    def __str__(self):
        return self.name

class Conference(models.Model):
    title = models.CharField(max_length=100, null=False)
    host = models.CharField(max_length=100, null=False)
    concenor = models.CharField(max_length=100, null=False)
    content = models.TextField(null=False)
    issue = models.TextField(null=False)
    date = models.DateField(null=False)
    place = models.CharField(max_length=100, null=False)
    file = models.FileField(upload_to='uploads/', blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=True, null=False)

    def __str__(self):
        return self.title

class Conference_content(models.Model):
    recorder = models.CharField(max_length=100, null=False)
    time = models.CharField(max_length=100, null=False)
    content = models.TextField(null=False)
    file = models.FileField(upload_to='uploads/', blank=True, null=True)
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE, default=True)


class Participant(models.Model):
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE, default=True)
    member = models.ForeignKey(Account, on_delete=models.CASCADE, default=True)
    
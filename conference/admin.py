from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Conference, Conference_content,Project,Participant
# Register your models here.

admin.site.register(Conference)
admin.site.register(Conference_content)
admin.site.register(Project)
admin.site.register(Participant)


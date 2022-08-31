from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os

def file(request):
    if request.method=="POST":
        uploaded_file = request.FILES['file']
        fss = FileSystemStorage()
        file = fss.save(uploaded_file.name, uploaded_file)
        return redirect("file")
    mediafiles = os.listdir(settings.MEDIA_ROOT)        
    return render(request, "file.html", locals(mediafiles))

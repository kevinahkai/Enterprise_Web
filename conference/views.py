from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ConferenceForm, ProjectForm
from .models import Conference, Conference_content,Project

def index(request):
    return HttpResponse(f"conference page.")

def conference_list(request):
    conference = Conference.objects.all()
    form = ConferenceForm()
    if request.method == "POST":
        form = ConferenceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form)
        return redirect("conference_list")    #跳到哪個頁面  
    context = {
        'conference' : conference,
        'form': form,
    }

    return render(request, 'conference/conference_list.html', context)

def conference_content(request, pk):
    conference = Conference.objects.get(id=pk)
    form = ConferenceForm(instance=conference)
    if request.method == 'POST':
        if request.POST.get('recorder') and request.POST.get('time') and request.POST.get('content') or request.POST.get('file'):
            content = Conference_content()
            content.recorder = request.POST.get('recorder')
            content.time = request.POST.get('time')
            content.content = request.POST.get('content')
            content.file = request.POST.get('file')
            content.save()
            return redirect("conference_content", pk)
        else:
            return redirect("conference_content")
    context = {
        'conference' : conference,
        'form': form,
    }
    
    return render(request, 'conference/conference_content.html', context)


def conference_delete(request, pk):
    conference = Conference.objects.get(id=pk)
    if request.method == "POST":
        conference.delete()
        return redirect("conference_list")

    context = {
        'conference' : conference
    }

    return render(request, 'conference/conference_delete.html', context)

def project_list(request):
    project = Project.objects.all()
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form)
        return redirect("project_list")
    context = {
        'project' : project,
        'form' : form,
    }
    
    return render(request, 'conference/project_list.html', context)

def project_content(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    context = {
        'project' : project,
        'form' : form,
    }
    return render(request, 'conference/project_content.html', context)

def project_delete(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect("project_list")
    
    context = {
        'project' : project
    }

    return render(request, 'conference/project_delete.html', context)

def eerror(request):
    context = {}
    return render(request, "error.html", context)
    

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

def index(request):
    template = loader.get_template('indexs.html')
    return HttpResponse(template.render())

@login_required
def topics(request):
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    template = loader.get_template('topics.html')
    return HttpResponse(template.render(context, request))

@login_required
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    template = loader.get_template('topic.html')
    return HttpResponse(template.render(context, request))

@login_required
def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('topics'))

    context = {'form': form}
    template = loader.get_template('new_topic.html')
    return HttpResponse(template.render(context, request))

@login_required
def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id) # 使用topic_id來取得正確主題物件
    
    if request.method != 'POST':
        form = EntryForm()        
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('topic',args=[topic_id]))
    
    context = {'topic': topic, 'form': form}
    template = loader.get_template('new_entry.html')
    return HttpResponse(template.render(context, request))

@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topic',args=[topic.id]))
    
    context = {'entry': entry, 'topic': topic, 'form': form}
    template = loader.get_template('edit_entry.html')
    return HttpResponse(template.render(context, request))
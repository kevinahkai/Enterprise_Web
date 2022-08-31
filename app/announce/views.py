from multiprocessing import context
from django.views.generic import ListView
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NewsForm
from .models import News
from django.contrib.auth.decorators import login_required, permission_required

def index(request):
    return render(request, 'index.html')

@login_required()
def read(request):
    department = request.user.department
    if department == 'GM':
        news = News.objects.all()
    else:
        news = News.objects.filter(department = department)

    form = NewsForm()

    if request.method == "POST":
        if request.user.is_authenticated and request.user.has_perm('announce.add_news'):
            form = NewsForm(request.POST, request.FILES)
            if form.is_valid():
                announce = form.save(commit=False)
                announce.owner = request.user
                announce.department = department
                announce.save()
            return redirect("read")    #跳到哪個頁面
        else:
            return redirect("read")

    context = {
        'news' : news,
        'form': form,
    }

    return render(request, 'read.html', context)

def detail(request, pk):
    news = News.objects.get(id=pk)
    form = NewsForm(instance=news)

    if request.method == "POST":
        if request.user.is_authenticated and request.user.has_perm('announce.change_news'):
            form = NewsForm(request.POST, request.FILES, instance=news)
            if form.is_valid():
                form.save()

            return redirect("detail", pk)
        else:
            return redirect("read")

    context = {
        'form': form,
        'news' : news,
    }

    return render(request, 'detail.html', context)

@permission_required("announce.delete_news", login_url='read')
def delete(request, pk):
    news = News.objects.get(id=pk)

    if request.method == "POST":
        news.delete()
        return redirect('read')

    context = {
        'news':news
    }

    return render(request, 'delete.html', context)

def eerror(request):
    context = {}
    return render(request, "error.html", context)

def SearchResults(request):
    query = request.GET.get("department")
    news = News.objects.filter( department__startswith = query )

    context = {
        'new' : news,
    }

    return render(request, 'search_results.html', context)
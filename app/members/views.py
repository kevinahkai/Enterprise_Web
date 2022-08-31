from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout

from .forms import RegistrationForm, AccountAuthenticationForm

def register_view(request, *args, **kwargs): #註冊業
    user = request.user
    if user.is_authenticated: #已經登入使用者
        return HttpResponse(f"You are already authenticated as {user.email}.")

    context={}

    if request.method == 'POST':
        form = RegistrationForm(request.POST or None) #創建表單

        if form.is_valid(): #確認表單都正常
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            destination = get_redirect_if_exists(request)
            if destination:
                return redirect(destination)
            return redirect("read")
        else:
            context['registration_form'] = form

    return render(request, 'register.html', context)

def login_view(request, *args, **kwargs):
    
    context={}

    user = request.user
    if user.is_authenticated:
        return redirect("read")

    destination = get_redirect_if_exists(request)
    if request.method == "POST":
        form = AccountAuthenticationForm(request.POST or None)
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user:
            login(request, user)
            destination = get_redirect_if_exists(request)
            if destination:
                return redirect(destination)
            return redirect("read")

        else:
            context['login_form'] = 'Email or password error'

    return render(request, "login.html", context)

def logout_view(request):
    logout(request)
    return redirect("index")

def get_redirect_if_exists(request):
    redirect = None
    if request.GET:
        if request.GET.get("next"):
            redirect = str(request.GET.get("next"))
    return redirect



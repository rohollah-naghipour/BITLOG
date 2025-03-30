
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import messages

from products.forms import RegistrationForm
from products.models import *


def register_view(request):
    form = RegistrationForm()

    if request.method == 'POST':
        if form.is_valid(): 
            form.save()
            print("here")
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(username)
            print(password)
            user = authenticate(username=username, password=password)
            print(user)
            messages.success(request, "ثبت نام با موفقیت انجام شد.")
            return redirect('home') 
        else:
            return render(request, 'register.html', {'form': form})
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})



class Login(TemplateView):
    template_name = 'login.html'
  


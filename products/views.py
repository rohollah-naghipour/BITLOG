from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from django import forms
from django.contrib.auth import authenticate, login 
from django.contrib.auth.hashers import check_password
from django.db.models import Q
from products.models import *
from .forms import RegistrationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
from .models import Article
import re as r
from .forms import RegistrationForm
from django.contrib.auth import login


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

@login_required
def article_create_update(request, pk=None):
    if pk:
        article = get_object_or_404(Article, pk=pk, author=request.user)
    else:
        article = None

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('home')  
    else:
        form = ArticleForm(instance=article)
    return render(request, 'article_form.html', {'form': form})


#def register_view(request):
    #if request.method == 'POST':
        #form = RegistrationForm(request.POST)
        #if form.is_valid():
            #user = form.save()  # Save the user object
            #login(request, user)
            #messages.success(request, "ثبت نام با موفقیت انجام شد.")
            #return redirect('profile')  # Redirect to profile page or another appropriate page after registration
        #else:
            #return render(request, 'register.html', {'form': form})
    #else:
        #form = RegistrationForm()
    #return render(request, 'register.html', {'form': form})



    #def get(self, request, **kwargs):
        #if request.method == "POST":
            #form = register(request.POST)
            
            #if form.is_valid():
                #return redirect("home")
            #else:
                #form = register()
        #return render(request, "register.html", {"form": form})


class Login(TemplateView):
    template_name = 'login.html'
  

class CategoryPage(TemplateView):
    def get(self, request, **kwargs):
        categories = Category.objects.all()
        return render(request, 'category-summary.html', {'categories': categories})  
    
class CategoryView(TemplateView):
    def get(self, request, cat):
        cat = r.sub(r'[-_]+', ' ', cat).strip().title()
        
        try:
            category = Category.objects.get(title__iexact=cat)
            articles = Article.objects.filter(category=category)

            context = {
                'category': category,
                'articles': articles}
        
            return render(request, 'category.html', context)
            
        except Category.DoesNotExist:
            messages.error(request, f"دسته‌بندی '{cat}' یافت نشد")
            
            return render(request, 'category-summary.html')

class SingleArticle(TemplateView):
    def get(self, request, cat):
        try:
            cat = r.sub(r'[-_]+', ' ', cat).strip().title()

            articles = Article.objects.filter(title__iexact = cat)
            return render(request, 'single-article.html', {'articles': articles})
        
        except articles.DoesNotExist:
            return render(request, '404.html', {'message': f"دسته‌بندی '{cat}' یافت نشد"}, status=404)
                

class Indexpage(TemplateView):
    def get(self, request, **kwargs):
        
        article_data = []
        all_articles = Article.objects.all().order_by('-created_at')[:12]

        for article in all_articles:
            article_data.append({
                'title': article.title,
                'cover': article.cover.url,
                'category': article.category.title,
                'created_at': article.created_at.date(),
            })
        
        promote_data = []
        all_promote_articles = Article.objects.filter(promote=True)

        for promote_article in all_promote_articles:
            promote_data.append({
                'category': promote_article.category.title,
                'title': promote_article.title,
                'author': promote_article.author.user.username,
                'avatar': promote_article.author.avatar.url if promote_article.author.avatar else None,
                'cover': promote_article.cover.url if promote_article.cover else None,
                'created_at': promote_article.created_at.date(),
            })

        context = {
            'article_data': article_data,
            'promote_article_data': promote_data,
        }

        return render(request, 'index.html', context)



class ContactPage(TemplateView):
    template_name = "page-contact.html"



class AboutPage(TemplateView):
    template_name = 'page-about.html'

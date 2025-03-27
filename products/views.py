from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages

import re as r

from products.models import *






class Login(TemplateView):
    template_name = 'login.html'

class Register(TemplateView):
    template_name = 'register.html'



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

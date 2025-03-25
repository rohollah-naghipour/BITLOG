from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from products.models import *
from django.contrib import messages


class ContactPage(TemplateView):
    template_name = "page-contact.html"

class AboutPage(TemplateView):
    template_name = 'page-about.html'

#def category_summary(request):
    """Display a list of all Categories"""
    #categories = Category.objects.all()
    #context = {"categories":categories}
    #return render(request, 'category-summary.html', context)

class CategoryPage(TemplateView):
    def get(self, request, **kwargs):
        categories = Category.objects.all()
        return render(request, 'category-summary.html', {'categories': categories})  
     

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Category, Article
import re

def category(request, cat):
    """نمایش مقالات یک دسته‌بندی خاص"""
    # پردازش عنوان فارسی
    cat = re.sub(r'[-_]+', ' ', cat).strip().title()
    
    try:
        # جستجو با عنوان فارسی
        category = Category.objects.get(title__iexact=cat)
        articles = Article.objects.filter(category=category)
        
        return render(request, 'category.html', {
            'category': category,
            'articles': articles
        })
        
    except Category.DoesNotExist:
        messages.error(request, f"دسته‌بندی '{cat}' یافت نشد")
        return render(request, 'category-summary.html')


def SingleArticle(request, cat):
    try:
        cat = re.sub(r'[-_]+', ' ', cat).strip().title()

        articles = Article.objects.filter(title__iexact = cat)
        return render(request, 'single-article.html', {'articles': articles})
    
    except articles.DoesNotExist:
        return render(request, '404.html', {'message': f"دسته‌بندی '{cat}' یافت نشد"}, status=404)


#def SingleArticle(request, cat):
    #cat = re.sub(r'[-_]+', ' ', cat).strip().title()

    #category = Category.objects.get(title__iexact=cat)
    #print(category)
    #articles = Article.objects.filter(category=category)
    #print(articles)
    
    #return render(request, 'single-article.html', {'articles': articles})
        
 
  


#def category(request, cat):
    """Refine items to a category"""
    # Replace hyphens with spaces
   # cat = cat.replace('-', ' ').title()
   # print(f"cat after .replace: {cat}")
    
   # try:
       # category =  Category.objects.get(name=cat)
       # print(category)
       # Articles =  Article.objects.filter(category=category)
       # print(Articles)
       # return render(request, 'category.html', {"category": category,"Articles":Articles})
   # except:
       #messages.error(request, ("That category doesn't exist")) 
       #return render(request, 'category-summary.html')
           
        
        

class Indexpage(TemplateView):
    #template_name = "index.html"
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

        #profile_name_search = Article.objects.get(profile_name=)
        #user_avatar = User.objects.all() #(user=profile_name_search.user.pk)
        #for p in all_promote_articles: 
            #print(p.author.user.username, "firstname")
        #print(user_avatar.user.last_name)

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



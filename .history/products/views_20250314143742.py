from django.shortcuts import render
from django.views.generic import TemplateView
from products.models import *


class ContactPage(TemplateView):
    template_name = "page-contact.html"

#class AboutPage(TemplateView):
    #template_name = 'page-about.html'

#class CategoryPage(TemplateView):
    #template_name = 'category.html'




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



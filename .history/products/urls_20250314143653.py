
from django.urls import path
from products import views

urlpatterns = [
    path("home/", views.Indexpage.as_view(), name='home'),
    path("contact/",views.ContactPage.as_view(), name = 'contact'),
    #path('about/', views.AboutPage.as_view(), name='about'),
    #path('category/', views.CategoryPage.as_view(), name = 'category'),

]


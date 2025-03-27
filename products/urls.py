
from django.urls import path
from products import views

urlpatterns = [
    path("", views.Indexpage.as_view(), name='home'),
    path("contact/",views.ContactPage.as_view(), name = 'contact'),
    path("about/", views.AboutPage.as_view(), name='about'),
    path("category-summary/", views.CategoryPage.as_view(), name = 'category-summary'),
    path('category/<str:cat>', views.CategoryView.as_view(), name = 'category'),
    path('single-article/<str:cat>', views.SingleArticle.as_view(), name = 'single-article'),
    path('login/', views.Login.as_view(), name = 'login'),
    path('register/', views.Register.as_view(), name = 'register'),
]

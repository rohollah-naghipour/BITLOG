
from django.urls import path
from products import views

urlpatterns = [
    path("", views.Indexpage.as_view(), name='home'),
    path("contact/",views.ContactPage.as_view(), name = 'contact'),
    path("about/", views.AboutPage.as_view(), name='about'),
    path("category-summary/", views.CategoryPage.as_view(), name = 'category-summary'),
    path('category/<str:cat>', views.category, name = 'category'),
]

    #path('category/<str:cat>', views.category, name='category'),
    #path('category-summary/', views.category_summary, name='category-summary'),
    
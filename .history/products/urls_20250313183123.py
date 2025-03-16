
from django.urls import path
from products import views

urlpatterns = [
    path("home", views.Indexpage.as_view(), name='home'),
    path("contact/",views.ContactPage.as_view(), name = 'contact'),

]

 #url(r'^contact/$', views.ContactPage.as_view(), name='contact'),
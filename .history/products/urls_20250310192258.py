
from django.urls import path
from products import views

urlpatterns = [
    path("Home", views.Indexpage.as_view(), name = 'index')

]


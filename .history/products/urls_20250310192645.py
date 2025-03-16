
from django.urls import path
from products import views

urlpatterns = [
    path("home", views.Indexpage.as_view(), name='home')

]


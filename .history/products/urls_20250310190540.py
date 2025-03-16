
from django.urls import path
from products import views

urlpatterns = [
    path("", views.Indexpage.as_view(), name = 'index')

]


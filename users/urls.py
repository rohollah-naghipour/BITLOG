
from django.urls import path
from users import views

urlpatterns = [
   path('login/', views.Login.as_view(), name = 'login'),
   path('register/', views.register_view, name = 'register'),
]


from django.contrib import admin
from django.urls import path, include
from products.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    path("", include('products.urls'))
]

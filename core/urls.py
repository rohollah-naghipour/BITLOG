
from django.contrib import admin
from django.urls import path, include
from products.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    path("", include('products.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static('contact/static',document_root=settings.STATIC_ROOT)
    urlpatterns += static('about/', document_root=settings.STATIC_ROOT)
    urlpatterns += static('category-summary/', document_root=settings.STATIC_ROOT)
    urlpatterns += static('article/<int:pk>/delete/', document_root=settings.STATIC_ROOT)

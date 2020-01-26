from django.conf.urls import include

from django.contrib import admin
from django.urls import path

from categories import urls as categories_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categories/', include(categories_urls)),
]

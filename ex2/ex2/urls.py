from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('vaccines/', include('vaccines.urls')),
    path('admin/', admin.site.urls),
]
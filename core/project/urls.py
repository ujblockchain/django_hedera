from django.contrib import admin
from django.urls import include, path

from core.project.settings import ADMIN_PATH

urlpatterns = [
    path(f'{ADMIN_PATH}/', admin.site.urls),
    path('', include('core.contacts.urls')),
]

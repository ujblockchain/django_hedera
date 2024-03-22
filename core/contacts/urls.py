from django.urls import path

from .views import ContactDetails, ContactHome

urlpatterns = [
    path('', ContactHome.as_view(), name='home'),
    path('<int:pk>/details/', ContactDetails.as_view(), name='details'),
]

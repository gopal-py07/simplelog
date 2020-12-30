
from django.urls import path
from .import views

urlpatterns = [
    path('l/',views.flog),
   path('mail/',views.sendmail)
]
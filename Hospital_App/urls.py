from django.urls import path
from Hospital_App.views import home
urlpatterns = [
    path('', home),
]
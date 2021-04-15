from django.urls import path
from Hospital_App.views import home, hospital
urlpatterns = [
    path('', home),
    path('hospital', hospital, name = 'hospital-url')
]

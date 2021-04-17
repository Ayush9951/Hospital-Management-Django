from django.urls import path
from Hospital_App.views import home, hospital, patients
urlpatterns = [
    path('', home),
    path('hospital', hospital, name = 'hospital-url'),
    path('hospital/patients/', patients, name = 'patients-url')

]

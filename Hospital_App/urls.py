from django.urls import path
from Hospital_App.views import home, hospital, patients, delete_patient, update_patient
urlpatterns = [
    path('', home),
    path('hospital', hospital, name = 'hospital-url'),
    path('hospital/patients/', patients, name = 'patients-url'),
    path('hospital/patients/delete/<int:id>/', delete_patient, name = 'delete-patient-url'),
    path('hospital/patients/update/<int:id>/', update_patient, name = 'update-patient-url'),

]

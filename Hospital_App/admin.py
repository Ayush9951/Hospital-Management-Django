from django.contrib import admin

from Hospital_App.models.patient import Patient

class PatientAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'city', 'phone', 'date']

admin.site.register(Patient, PatientAdmin)
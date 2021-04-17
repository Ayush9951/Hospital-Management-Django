from django.shortcuts import render,redirect
from Hospital_App.models.patient import Patient

def home(request):
    return render(request, 'index.html')

def hospital(request):
    return render(request, 'hospital/hospital.html')

def patients(request):
     if request.method == 'POST':

        patient = Patient()
        patient_name = request.POST.get('patient-name')
        patient_age = request.POST.get('patient-age')
        patient_city = request.POST.get('patient-city')
        patient_phone = request.POST.get('patient-phone')
        date = request.POST.get('date')

        if len(patient_name) > 0 and len(patient_age) > 0 and len(patient_city) > 0 and len(patient_phone) > 0:
            patient = Patient(name = patient_name,age = patient_age, city = patient_city, phone = patient_phone, date=date)
            patient.save()
            return redirect('/hospital/patients')

     patient_details = Patient.objects.all()
     return render(request, 'hospital/patients/patients.html', {'patient_details': patient_details})


def delete_patient(request,id):
    if request.method == 'POST':
        patient_delete = Patient(pk=id) 
        patient_delete.delete()
        return redirect('/hospital/patients')

    patient_details = Patient.objects.all()
    return render(request, 'hospital/patients/patients.html', {'patient_details': patient_details})

def update_patient(request,id):
    if request.method == 'POST':
        patient_update_details = Patient.objects.get(pk=id)
        return render(request, 'hospital/patients/patient-update-form.html',{'patient_update_details' : patient_update_details})

    elif request.method == "GET":
        patient = Patient()

        patient_name = request.GET.get('update-patient-name')
        patient_age = request.GET.get('update-patient-age')
        patient_city = request.GET.get('update-patient-city')
        patient_phone = request.GET.get('update-patient-phone')
        date = request.GET.get('update-date')

        patient = Patient(pk=id,name = patient_name, age = patient_age, city = patient_city, phone = patient_phone,date=date)
        patient.save()  
        return redirect('/hospital/patients')
    
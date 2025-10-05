from django.shortcuts import render,redirect
from myapp.models import *

# Create your views here.

def homepage(request):

    return render(request,"home.html")

def departmentpage(request):
    if request.method=='POST':
        name=request.POST.get('name')
        location=request.POST.get('location')   
        dept_data=Departmentmodel.objects.get(id=name)
        Departmentmodel.objects.create(
            name=name,
            location=location,      
            dept_data=dept_data,
        )
    department_data=Departmentmodel.objects.all()
    context={
        'department_data':department_data
    }   
    return render(request,"department.html",context)

def doctorpage(request):
    dept = Departmentmodel.objects.all()
    if request.method =='POST':
        print("works")
        name=request.POST.get('name')
        Specialization=request.POST.get('Specialization')
        phone=request.POST.get('phone')
        email=request.POST.get('email') 
        doc_id=request.POST.get('department_data')
        department_data=Departmentmodel.objects.get(id=doc_id)

        Doctormodel.objects.create(
            name=name,
            specialization=Specialization,
            phone=phone,
            email=email,
            department=department_data,
        )
        return redirect('doctorpageurl')
    department_data=Departmentmodel.objects.all()
    doctor_data=Doctormodel.objects.all()

    context={
        'department_data':dept,
        'doctor_data':doctor_data
        }

    return render(request,"doctor.html",context)

def patientpage(request):

    if request.method=='POST':
        doctor_name=request.POST.get('name')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        doctor_id=request.POST.get('doctor_id')
        doctor_data=Doctormodel.objects.get(id=doctor_id)

        Patientmodel.objects.create (#data save
            name=doctor_name,
            age=age,
            gender=gender,
            phone=phone,
            address=address,
            doctor=doctor_data
        )
        return redirect('patientpageurl')
    doctor_data=Doctormodel.objects.all()
    patient_data=Patientmodel.objects.all()
    context={
        'doctor_data':doctor_data,
        'patient_data':patient_data
    }
    return render(request,"patient.html",context)

def appointmentpage(request):
    if request.method=='POST':
        patient_id=request.POST.get('patient')
        doctor_id=request.POST.get('doctor')
        appointment_date=request.POST.get('appointment_date')
        status=request.POST.get('status')
       
        patient_name=Patientmodel.objects.get(id=patient_id)
        doctor_name=Doctormodel.objects.get(id=doctor_id)
        

        Appointmentmodel.objects.create(
            patient=patient_name,
            doctor=doctor_name,
            appointment_date=appointment_date,
            status=status,
        )
        return redirect('appointmentpageurl')
   
    patient_data=Patientmodel.objects.all()
    doctor_data=Doctormodel.objects.all()
    appointment_data=Appointmentmodel.objects.all()
    context={
         'patient_data':patient_data,
        'appointment_data':appointment_data,
        'doctor_data':doctor_data
                }
    return render(request,"appointment.html",context)




def doctordeletepage(request,id):
    delete_data=Doctormodel.objects.get(id=id)
    delete_data.delete()
    return redirect('doctorpageurl')




def doctoreditpage(request,id):
    edit_data=Doctormodel.objects.get(id=id)
    edit_data.edit()
    return redirect("editpageurl")



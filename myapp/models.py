from django.db import models

class Departmentmodel(models.Model):
    name=models.CharField(null=True, max_length=1000)
    location=models.CharField(null=True, max_length=100)
    def __str__(self):
        return self.name

class Doctormodel(models.Model):
    SPECIALIZATION_CHOICE=[

        ('Cardiology','Cardiology'),
        ('Dermatology','Dermatology'),
        ('Pediatrics','Pediatrics'),
        ('Oncology','Oncology'),
    ]

    name=models.CharField(null=True, max_length=50)
    specialization=models.CharField(max_length=100,choices= SPECIALIZATION_CHOICE,null=True)
    phone=models.CharField(null=True, max_length=15)
    email=models.EmailField(null=True, max_length=254)
    department=models.ForeignKey(Departmentmodel, on_delete=models.SET_NULL,null=True,related_name="doctor")
    def __str__(self):
        return self.department.name



class Patientmodel(models.Model):
     
     GENDER_CHOICES=[
        ( 'Male','Male'),
        ( 'Female','Female'),
        ( 'others','others'),

     ]
     name=models.CharField(null=True, max_length=50)
     age=models.IntegerField(null=True)
     gender=models.CharField(choices=GENDER_CHOICES, max_length=50,null=True)
     phone=models.CharField(null=True, max_length=15)
     address=models.TextField(null=True) 
     doctor=models.ForeignKey(Doctormodel, on_delete=models.CASCADE,related_name="patient") 
     def __str__(self):
        return self.doctor.name

class Appointmentmodel(models.Model):
     STATUS_CHOICES=[
          ("Pending","Pending"),
          ("Completed","Completed"),
          ("Cancelled","Cancelled"),

     ]
     
     patient=models.ForeignKey(Patientmodel, on_delete=models.CASCADE,)
     doctor=models.ForeignKey(Doctormodel, on_delete=models.CASCADE)
     appointment_date=models.DateField(null=True)
     status=models.CharField(choices= STATUS_CHOICES, null=True, max_length=50,default="Pending")
     def __str__(self):
        return self.patient.name
     







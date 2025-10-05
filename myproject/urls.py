
from django.contrib import admin
from django.urls import path

from myapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepageurl'),
    path('doctor/', doctorpage, name='doctorpageurl'),   
    path('department/', departmentpage, name='departmentpageurl'),
    path('patient/', patientpage, name='patientpageurl'),
    path('appointment/', appointmentpage, name='appointmentpageurl'),
    path('delete/,<int:id>',doctordeletepage,name="deletepageurl"),
    path('Edit/,<int:id>',doctoreditpage,name="editpageurl"),
]

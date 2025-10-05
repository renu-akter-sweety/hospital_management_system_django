# hospital_management_system_django
Hospital Management System 
Models 
1. Department 
o name (CharField) 
o location (CharField) 
2. Doctor 
o name (CharField) 
o specialization (Select Key) 
o phone (CharField) 
o email (EmailField) 
o department (ForeignKey) 
3. Patient 
o name (CharField) 
o age (IntegerField) 
o gender (CharField with choices: Male, Female, Other) 
o phone (CharField) 
o address (TextField) 
o doctor (ForeignKey ) 
4. Appointment 
o patient (ForeignKey → Patient) 
o doctor (ForeignKey → Doctor) 
o appointment_date (DateTimeField) 
o status (CharField with choices: Pending, Completed, Cancelled) 
Tasks 
1. Implement CRUD operations for all models (Department, Doctor, Patient, 
Appointment). 
2. Relationship handling: 
o Each department can have many doctors. 
o Each doctor can have many patients. 
o Each patient can book many appointments with a doctor. 
3. Create pages to: 
o View all doctors under a department. 
o View all patients of a doctor. 
o View all appointments of a patient. 
4. Bonus: 
o When a doctor is deleted, their patients and appointments should also be deleted 
(on_delete=CASCADE). 
o Display a doctor’s profile showing their department, patients, and upcoming 
appointments.

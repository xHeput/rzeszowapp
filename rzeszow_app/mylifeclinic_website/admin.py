from django.contrib import admin
from .models import Adress, Appointment, Department, Employee, HospitalReferral, Medicine, Patient, Permissions, PermissionsEmployee, PermissionsPatient, Position, Prescription, PrescriptionMedicine


# Add here whatever you need in admin Panel to see
admin.site.register(Adress)
admin.site.register(Appointment)
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(HospitalReferral)
admin.site.register(Medicine)
admin.site.register(Patient)
admin.site.register(Permissions)
admin.site.register(PermissionsEmployee)
admin.site.register(PermissionsPatient)
admin.site.register(Position)
admin.site.register(Prescription)
admin.site.register(PrescriptionMedicine)
# Register your models here.

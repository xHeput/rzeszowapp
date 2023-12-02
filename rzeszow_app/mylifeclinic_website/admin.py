from django.contrib import admin
from .models import Appointment, Patient, Employee, Position
# Register your models here.

admin.site.register(Appointment)
admin.site.register(Patient)
admin.site.register(Employee)
admin.site.register(Position)



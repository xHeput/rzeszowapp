# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Adress(models.Model):
    miasto = models.CharField(max_length=50, blank=True, null=True)
    wojewodztwo = models.CharField(max_length=50, blank=True, null=True)
    kraj = models.CharField(max_length=50, blank=True, null=True)
    ulica = models.CharField(max_length=50, blank=True, null=True)
    numer_domu = models.CharField(max_length=50, blank=True, null=True)
    numer_mieszkania = models.CharField(max_length=50, blank=True, null=True)
    kod_pocztowy = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adress'


class Appointment(models.Model):
    date_of = models.DateField(blank=True, null=True)
    opis = models.CharField(max_length=255)
    hospital_referral = models.ForeignKey('HospitalReferral', models.DO_NOTHING)
    patient = models.ForeignKey('Patient', models.DO_NOTHING)
    prescription = models.ForeignKey('Prescription', models.DO_NOTHING)
    employee = models.ForeignKey('Employee', models.DO_NOTHING)
    department = models.ForeignKey('Department', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'appointment'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Department(models.Model):
    nazwa = models.CharField(max_length=255)
    adress = models.ForeignKey(Adress, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'department'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Employee(models.Model):
    email = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    imie = models.CharField(max_length=50, blank=True, null=True)
    nazwisko = models.CharField(max_length=70, blank=True, null=True)
    numer_tel = models.CharField(max_length=15, blank=True, null=True)
    postion = models.ForeignKey('Position', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'employee'


class HospitalReferral(models.Model):
    opis = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hospital_referral'


class Medicine(models.Model):
    nazwa = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'medicine'


class MylifeclinicWebsiteAppointment(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_of = models.DateField()
    patient = models.OneToOneField('MylifeclinicWebsitePatient', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mylifeclinic_website_appointment'


class MylifeclinicWebsiteEmployee(models.Model):
    id = models.BigAutoField(primary_key=True)
    position = models.ForeignKey('MylifeclinicWebsitePosition', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mylifeclinic_website_employee'


class MylifeclinicWebsitePatient(models.Model):
    id = models.IntegerField(primary_key=True)
    imie = models.CharField(max_length=70)
    nazwisko = models.CharField(max_length=70)
    employee = models.OneToOneField(MylifeclinicWebsiteEmployee, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mylifeclinic_website_patient'


class MylifeclinicWebsitePosition(models.Model):
    id = models.IntegerField(primary_key=True)
    nazwa = models.CharField(max_length=70)

    class Meta:
        managed = False
        db_table = 'mylifeclinic_website_position'


class Patient(models.Model):
    email = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=70, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    pesel = models.CharField(max_length=11, blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    adress = models.ForeignKey(Adress, models.DO_NOTHING)

    def __str__(self):
        return (f"{self.first_name}")

    class Meta:
        managed = False
        db_table = 'patient'


class Permissions(models.Model):
    nazwa = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'permissions'


class PermissionsEmployee(models.Model):
    permissions = models.ForeignKey(Permissions, models.DO_NOTHING)
    employee = models.ForeignKey(Employee, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'permissions_employee'


class PermissionsPatient(models.Model):
    permissions = models.ForeignKey(Permissions, models.DO_NOTHING)
    patient = models.ForeignKey(Patient, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'permissions_patient'


class Position(models.Model):
    nazwa = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'position'


class Prescription(models.Model):
    nazwa = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prescription'


class PrescriptionMedicine(models.Model):
    medicine = models.ForeignKey(Medicine, models.DO_NOTHING)
    prescription = models.ForeignKey(Prescription, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'prescription_medicine'

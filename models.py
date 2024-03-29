# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Administrator(models.Model):
    a_id = models.CharField(db_column='A_Id', primary_key=True, max_length=6)  # Field name made lowercase.
    a_password = models.CharField(db_column='A_password', max_length=45)  # Field name made lowercase.
    a_cnic = models.CharField(db_column='A_cnic', max_length=14)  # Field name made lowercase.
    a_name = models.CharField(db_column='A_name', max_length=45)  # Field name made lowercase.
    a_salary = models.IntegerField(db_column='A_salary')  # Field name made lowercase.
    a_age = models.IntegerField(db_column='A_age')  # Field name made lowercase.
    a_sex = models.CharField(db_column='A_sex', max_length=10)  # Field name made lowercase.
    a_address = models.CharField(db_column='A_address', max_length=45)  # Field name made lowercase.
    a_email = models.CharField(db_column='A_email', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'administrator'


class AdmissionDetails(models.Model):
    data_admitted = models.DateTimeField()
    date_discharge = models.DateTimeField()
    p = models.OneToOneField('Patient', models.DO_NOTHING, db_column='P_Id', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'admission_details'


class Appointment(models.Model):
    a_date = models.CharField(db_column='A_Date', max_length=10, blank=True, null=True)  # Field name made lowercase.
    a_time = models.CharField(db_column='A_Time', max_length=10, blank=True, null=True)  # Field name made lowercase.
    p = models.ForeignKey('Patient', models.DO_NOTHING, db_column='P_Id')  # Field name made lowercase.
    d = models.ForeignKey('Doctor', models.DO_NOTHING, db_column='D_Id')  # Field name made lowercase.
    p_name = models.CharField(max_length=45)

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
    dept_id = models.CharField(db_column='Dept_Id', primary_key=True, max_length=6)  # Field name made lowercase.
    dept_name = models.CharField(db_column='Dept_name', max_length=45)  # Field name made lowercase.
    d = models.ForeignKey('Doctor', models.DO_NOTHING, db_column='D_Id', blank=True, null=True)  # Field name made lowercase.

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


class Doctor(models.Model):
    d_id = models.CharField(db_column='D_Id', primary_key=True, max_length=6)  # Field name made lowercase.
    d_password = models.CharField(db_column='D_password', max_length=45)  # Field name made lowercase.
    d_cnic = models.CharField(db_column='D_cnic', max_length=14)  # Field name made lowercase.
    d_address = models.CharField(db_column='D_address', max_length=45)  # Field name made lowercase.
    d_name = models.CharField(db_column='D_name', max_length=45)  # Field name made lowercase.
    d_salary = models.IntegerField(db_column='D_salary')  # Field name made lowercase.
    d_age = models.IntegerField(db_column='D_age')  # Field name made lowercase.
    d_sex = models.CharField(db_column='D_sex', max_length=5)  # Field name made lowercase.
    d_senioritylevel = models.CharField(db_column='D_senioritylevel', max_length=10)  # Field name made lowercase.
    d_email = models.CharField(db_column='D_email', max_length=45)  # Field name made lowercase.
    dept = models.ForeignKey(Department, models.DO_NOTHING, db_column='Dept_Id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'doctor'


class LabTechnician(models.Model):
    l_id = models.CharField(db_column='L_Id', primary_key=True, max_length=6)  # Field name made lowercase.
    l_password = models.CharField(db_column='L_password', max_length=45)  # Field name made lowercase.
    l_cnic = models.CharField(db_column='L_cnic', max_length=14)  # Field name made lowercase.
    l_address = models.CharField(db_column='L_address', max_length=100)  # Field name made lowercase.
    l_name = models.CharField(db_column='L_name', max_length=45)  # Field name made lowercase.
    l_salary = models.IntegerField(db_column='L_salary')  # Field name made lowercase.
    l_age = models.IntegerField(db_column='L_age')  # Field name made lowercase.
    l_sex = models.CharField(db_column='L_sex', max_length=10)  # Field name made lowercase.
    l_senioritylevel = models.CharField(db_column='L_senioritylevel', max_length=45)  # Field name made lowercase.
    l_email = models.CharField(db_column='L_email', max_length=45)  # Field name made lowercase.
    lab = models.ForeignKey('Laboratories', models.DO_NOTHING, db_column='Lab_Id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lab_technician'


class Laboratories(models.Model):
    lab_id = models.CharField(db_column='Lab_Id', primary_key=True, max_length=6)  # Field name made lowercase.
    lab_name = models.CharField(db_column='Lab_name', max_length=45)  # Field name made lowercase.
    l = models.ForeignKey(LabTechnician, models.DO_NOTHING, db_column='L_Id', blank=True, null=True)  # Field name made lowercase.
    dept = models.ForeignKey(Department, models.DO_NOTHING, db_column='Dept_Id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'laboratories'


class Nurses(models.Model):
    n_cnic = models.CharField(db_column='N_cnic', primary_key=True, max_length=14)  # Field name made lowercase.
    n_name = models.CharField(db_column='N_name', max_length=45)  # Field name made lowercase.
    n_sex = models.CharField(db_column='N_sex', max_length=10, blank=True, null=True)  # Field name made lowercase.
    n_age = models.IntegerField(db_column='N_age')  # Field name made lowercase.
    n_salary = models.IntegerField(db_column='N_salary')  # Field name made lowercase.
    n_address = models.CharField(db_column='N_address', max_length=45, blank=True, null=True)  # Field name made lowercase.
    n_senioritylevel = models.CharField(db_column='N_senioritylevel', max_length=45, blank=True, null=True)  # Field name made lowercase.
    room = models.ForeignKey('Rooms', models.DO_NOTHING, db_column='room_Id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nurses'


class Patient(models.Model):
    p_id = models.CharField(db_column='P_Id', primary_key=True, max_length=6)  # Field name made lowercase.
    p_password = models.CharField(db_column='P_password', max_length=45)  # Field name made lowercase.
    p_cnic = models.CharField(db_column='P_cnic', max_length=14)  # Field name made lowercase.
    p_age = models.CharField(db_column='P_age', max_length=45)  # Field name made lowercase.
    p_address = models.CharField(db_column='P_address', max_length=45)  # Field name made lowercase.
    p_sex = models.CharField(db_column='P_sex', max_length=45)  # Field name made lowercase.
    p_name = models.CharField(db_column='P_name', max_length=45)  # Field name made lowercase.
    p_email = models.CharField(db_column='P_email', max_length=45)  # Field name made lowercase.
    room = models.ForeignKey('Rooms', models.DO_NOTHING, db_column='room_Id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'patient'


class Prescription(models.Model):
    tests = models.CharField(max_length=100, blank=True, null=True)
    medicine = models.CharField(max_length=45, blank=True, null=True)
    p = models.ForeignKey(Patient, models.DO_NOTHING, db_column='P_Id', blank=True, null=True)  # Field name made lowercase.
    d = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prescription'


class Qualification(models.Model):
    degrees = models.CharField(max_length=45, blank=True, null=True)
    d_id = models.CharField(db_column='D_Id', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'qualification'


class Rooms(models.Model):
    room_id = models.CharField(db_column='room_Id', primary_key=True, max_length=6)  # Field name made lowercase.
    room_type = models.CharField(max_length=45, blank=True, null=True)
    rate = models.IntegerField()
    n_cnic = models.ForeignKey(Nurses, models.DO_NOTHING, db_column='N_cnic', blank=True, null=True)  # Field name made lowercase.
    dept = models.ForeignKey(Department, models.DO_NOTHING, db_column='Dept_Id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rooms'


class TestReports(models.Model):
    r_name = models.CharField(db_column='R_name', max_length=45)  # Field name made lowercase.
    p_name = models.CharField(db_column='P_name', max_length=45)  # Field name made lowercase.
    t_name = models.CharField(db_column='T_name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    l_name = models.CharField(db_column='L_name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    result = models.CharField(db_column='Result', max_length=45, blank=True, null=True)  # Field name made lowercase.
    r_date = models.DateTimeField(db_column='R_date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'test_reports'


class Tests(models.Model):
    test_id = models.CharField(db_column='Test_Id', primary_key=True, max_length=6)  # Field name made lowercase.
    test_name = models.CharField(db_column='Test_name', max_length=45)  # Field name made lowercase.
    test_price = models.IntegerField(db_column='Test_price')  # Field name made lowercase.
    lab = models.ForeignKey(Laboratories, models.DO_NOTHING, db_column='Lab_Id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tests'

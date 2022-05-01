# Generated by Django 4.0.3 on 2022-04-30 09:33

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('a_id', models.CharField(db_column='A_Id', max_length=6, primary_key=True, serialize=False)),
                ('a_password', models.CharField(db_column='A_password', max_length=45)),
                ('a_cnic', models.CharField(db_column='A_cnic', max_length=14)),
                ('a_name', models.CharField(db_column='A_name', max_length=45)),
                ('a_salary', models.IntegerField(db_column='A_salary')),
                ('a_age', models.IntegerField(db_column='A_age')),
                ('a_sex', models.CharField(db_column='A_sex', max_length=10)),
                ('a_address', models.CharField(db_column='A_address', max_length=45)),
                ('a_email', models.CharField(db_column='A_email', max_length=45)),
            ],
            options={
                'db_table': 'administrator',
                'managed': False,
            },
            managers=[
                ('empAuth_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_date', models.DateField(blank=True, null=True, verbose_name='Appointment_Date(mm/dd/yyyy)')),
                ('a_time', models.TimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'appointment',
                'managed': False,
            },
            managers=[
                ('empAuth_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dept_id', models.CharField(db_column='Dept_Id', max_length=6, primary_key=True, serialize=False)),
                ('dept_name', models.CharField(db_column='Dept_name', max_length=45)),
            ],
            options={
                'db_table': 'department',
                'managed': False,
            },
            managers=[
                ('empAuth_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('d_id', models.CharField(db_column='D_Id', max_length=6, primary_key=True, serialize=False)),
                ('d_password', models.CharField(db_column='D_password', max_length=45)),
                ('d_cnic', models.CharField(db_column='D_cnic', max_length=14)),
                ('d_address', models.CharField(db_column='D_address', max_length=45)),
                ('d_name', models.CharField(db_column='D_name', max_length=45)),
                ('d_salary', models.IntegerField(db_column='D_salary')),
                ('d_age', models.IntegerField(db_column='D_age')),
                ('d_sex', models.CharField(db_column='D_sex', max_length=5)),
                ('d_senioritylevel', models.CharField(db_column='D_senioritylevel', max_length=10)),
                ('d_email', models.CharField(db_column='D_email', max_length=45)),
            ],
            options={
                'db_table': 'doctor',
                'managed': False,
            },
            managers=[
                ('empAuth_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Laboratories',
            fields=[
                ('lab_id', models.CharField(db_column='Lab_Id', max_length=6, primary_key=True, serialize=False)),
                ('lab_name', models.CharField(db_column='Lab_name', max_length=45)),
            ],
            options={
                'db_table': 'laboratories',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LabTechnician',
            fields=[
                ('l_id', models.CharField(db_column='L_Id', max_length=6, primary_key=True, serialize=False)),
                ('l_password', models.CharField(db_column='L_password', max_length=45)),
                ('l_cnic', models.CharField(db_column='L_cnic', max_length=14)),
                ('l_address', models.CharField(db_column='L_address', max_length=100)),
                ('l_name', models.CharField(db_column='L_name', max_length=45)),
                ('l_salary', models.IntegerField(db_column='L_salary')),
                ('l_age', models.IntegerField(db_column='L_age')),
                ('l_sex', models.CharField(db_column='L_sex', max_length=10)),
                ('l_senioritylevel', models.CharField(db_column='L_senioritylevel', max_length=45)),
                ('l_email', models.CharField(db_column='L_email', max_length=45)),
            ],
            options={
                'db_table': 'lab_technician',
                'managed': False,
            },
            managers=[
                ('empAuth_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Nurses',
            fields=[
                ('n_cnic', models.CharField(db_column='N_cnic', max_length=14, primary_key=True, serialize=False)),
                ('n_name', models.CharField(db_column='N_name', max_length=45)),
                ('n_sex', models.CharField(blank=True, db_column='N_sex', max_length=10, null=True)),
                ('n_age', models.IntegerField(db_column='N_age')),
                ('n_salary', models.IntegerField(db_column='N_salary')),
                ('n_address', models.CharField(blank=True, db_column='N_address', max_length=45, null=True)),
                ('n_senioritylevel', models.CharField(blank=True, db_column='N_senioritylevel', max_length=45, null=True)),
            ],
            options={
                'db_table': 'nurses',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('p_id', models.CharField(db_column='P_Id', max_length=6, primary_key=True, serialize=False)),
                ('p_password', models.CharField(db_column='P_password', max_length=45)),
                ('p_cnic', models.CharField(db_column='P_cnic', max_length=14)),
                ('p_age', models.CharField(db_column='P_age', max_length=45)),
                ('p_address', models.CharField(db_column='P_address', max_length=45)),
                ('p_sex', models.CharField(db_column='P_sex', max_length=45)),
                ('p_name', models.CharField(db_column='P_name', max_length=45)),
                ('p_email', models.CharField(db_column='P_email', max_length=45)),
            ],
            options={
                'db_table': 'patient',
                'managed': False,
            },
            managers=[
                ('empAuth_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tests', models.CharField(blank=True, max_length=100, null=True)),
                ('medicine', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'prescription',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degrees', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'qualification',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('room_id', models.CharField(db_column='room_Id', max_length=6, primary_key=True, serialize=False)),
                ('room_type', models.CharField(blank=True, max_length=45, null=True)),
                ('rate', models.IntegerField()),
            ],
            options={
                'db_table': 'rooms',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TestReports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_name', models.CharField(db_column='R_name', max_length=45)),
                ('result', models.CharField(blank=True, db_column='Result', max_length=45, null=True)),
                ('r_date', models.DateTimeField(blank=True, db_column='R_date', null=True)),
            ],
            options={
                'db_table': 'test_reports',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tests',
            fields=[
                ('test_id', models.CharField(db_column='Test_Id', max_length=6, primary_key=True, serialize=False)),
                ('test_name', models.CharField(db_column='Test_name', max_length=45)),
                ('test_price', models.IntegerField(db_column='Test_price')),
            ],
            options={
                'db_table': 'tests',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AdmissionDetails',
            fields=[
                ('data_admitted', models.DateTimeField()),
                ('date_discharge', models.DateTimeField()),
                ('p', models.OneToOneField(db_column='P_Id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='Hospital.patient')),
            ],
            options={
                'db_table': 'admission_details',
                'managed': False,
            },
        ),
    ]
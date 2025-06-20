# Generated by Django 5.2.2 on 2025-06-07 13:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mprf', '0012_mprfapply_resume'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant_name', models.CharField(max_length=100)),
                ('applicant_email', models.EmailField(max_length=254)),
                ('img_candidate', models.ImageField(upload_to='images')),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('resume', models.FileField(upload_to='resumes')),
                ('cover_letter', models.TextField(blank=True, null=True)),
                ('applied_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'In-Active')], default='active', max_length=20)),
                ('emergency_contact', models.CharField(blank=True, max_length=100, null=True)),
                ('pan_number', models.CharField(blank=True, max_length=20, null=True)),
                ('aadhaar_number', models.CharField(blank=True, max_length=20, null=True)),
                ('bank_account', models.CharField(blank=True, max_length=50, null=True)),
                ('ifsc_code', models.CharField(blank=True, max_length=20, null=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 5.2.2 on 2025-06-06 08:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mprf', '0004_skills'),
    ]

    operations = [
        migrations.CreateModel(
            name='MprfApply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant_name', models.CharField(max_length=100)),
                ('applicant_email', models.EmailField(max_length=254)),
                ('resume', models.FileField(upload_to='resumes/')),
                ('cover_letter', models.TextField(blank=True, null=True)),
                ('applied_on', models.DateTimeField(auto_now_add=True)),
                ('Skills', models.ManyToManyField(blank=True, to='mprf.skills')),
                ('mprf_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mprf.mprfrequest')),
            ],
        ),
    ]

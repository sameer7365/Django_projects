# Generated by Django 5.2.1 on 2025-06-03 06:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='todos.task'),
            preserve_default=False,
        ),
    ]

# Generated by Django 5.0.4 on 2024-04-29 04:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_visit_visit_date_time_alter_visit_doctor_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='visit',
            name='doctor',
        ),
    ]

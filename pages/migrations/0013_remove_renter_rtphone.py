# Generated by Django 4.1.4 on 2023-01-02 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0012_remove_attendance_spor_attendance_date_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="renter", name="Rtphone",),
    ]

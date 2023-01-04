# Generated by Django 4.1.4 on 2023-01-02 14:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0011_attendance_session_attendance_spor"),
    ]

    operations = [
        migrations.RemoveField(model_name="attendance", name="spor",),
        migrations.AddField(
            model_name="attendance",
            name="Date",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name="attendance",
            name="GroupTitle",
            field=models.CharField(
                max_length=100, null=True, verbose_name="Session Name"
            ),
        ),
    ]
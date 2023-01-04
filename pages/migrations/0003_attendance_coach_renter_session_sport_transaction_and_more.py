# Generated by Django 4.1.4 on 2023-01-02 12:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0002_player_address_player_email_player_fatherprof_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Attendance",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Date", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="Coach",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Name", models.CharField(max_length=100)),
                (
                    "Sport",
                    models.CharField(
                        choices=[
                            ("Football", "Football"),
                            ("Swimming", "Swimming"),
                            ("Karate", "Karate"),
                            ("Music", "Music"),
                            ("Art", "Art"),
                            ("Ladies Fitness", "Ladies Fitness"),
                        ],
                        max_length=50,
                        null=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Renter",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "RtName",
                    models.CharField(max_length=100, verbose_name="Renter Name"),
                ),
                ("Rtphone", models.IntegerField(verbose_name="Phone number")),
                (
                    "Fees",
                    models.DecimalField(
                        decimal_places=2, max_digits=3, verbose_name="Rent price"
                    ),
                ),
                (
                    "Location",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Stadium Day Full", "Stadium Day Full"),
                            ("Stadium Day Half", "Stadium Day Half"),
                            ("Stadium Night", "Stadium Night"),
                            ("SwPool Lane", "SwPool Lane"),
                            ("SwPool Half", "SwPool Half"),
                            ("SwPool Full", "SwPool Full"),
                        ],
                        max_length=100,
                        null=True,
                    ),
                ),
                ("RDuration", models.IntegerField(verbose_name="Rent Duration")),
                ("RDate", models.DateTimeField(verbose_name="Rent Date")),
            ],
        ),
        migrations.CreateModel(
            name="Session",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "SName",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Coral", "Coral"),
                            ("Guitar", "Guitar"),
                            ("Violine", "Violine"),
                            ("Act", "Act"),
                            ("Piano", "Piano"),
                        ],
                        max_length=100,
                        null=True,
                    ),
                ),
                ("Start", models.TimeField(verbose_name="Begin at")),
                ("End", models.TimeField(verbose_name="Ends at")),
                (
                    "Day",
                    models.CharField(
                        choices=[
                            ("Sun", "Sun"),
                            ("Mon", "Mon"),
                            ("Tus", "Tus"),
                            ("Wed", "Wed"),
                            ("Thu", "Thu"),
                            ("Fri", "Fri"),
                            ("Sat", "Sat"),
                        ],
                        max_length=100,
                        null=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Sport",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("SpName", models.CharField(max_length=100, verbose_name="Sport Name")),
                (
                    "PricMil",
                    models.DecimalField(
                        decimal_places=2, max_digits=3, verbose_name="Military price"
                    ),
                ),
                (
                    "PricCivil",
                    models.DecimalField(
                        decimal_places=2, max_digits=3, verbose_name="Civil price"
                    ),
                ),
                ("MinAge", models.IntegerField(verbose_name="Minimum Age")),
                ("MaxAge", models.IntegerField(verbose_name="Maximum Age")),
                ("Forl", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "TType",
                    models.CharField(
                        choices=[
                            ("Subscribe", "Subscribe"),
                            ("Renew", "Renew"),
                            ("Add Parent", "Add Parent"),
                        ],
                        max_length=100,
                        null=True,
                        verbose_name="Transaction Type",
                    ),
                ),
                (
                    "Fees",
                    models.DecimalField(decimal_places=2, max_digits=13, max_length=2),
                ),
                ("TDate", models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.RemoveField(model_name="player", name="Price",),
        migrations.AlterField(
            model_name="player",
            name="Brother",
            field=models.BooleanField(default=False, verbose_name="Have a brother"),
        ),
    ]

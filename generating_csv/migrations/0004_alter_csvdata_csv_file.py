# Generated by Django 4.1.7 on 2023-02-17 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("generating_csv", "0003_csvdata"),
    ]

    operations = [
        migrations.AlterField(
            model_name="csvdata",
            name="csv_file",
            field=models.FileField(upload_to=""),
        ),
    ]

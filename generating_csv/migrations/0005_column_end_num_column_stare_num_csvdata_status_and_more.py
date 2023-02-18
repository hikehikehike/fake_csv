# Generated by Django 4.1.7 on 2023-02-18 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("generating_csv", "0004_alter_csvdata_csv_file"),
    ]

    operations = [
        migrations.AddField(
            model_name="column",
            name="end_num",
            field=models.IntegerField(default=60),
        ),
        migrations.AddField(
            model_name="column",
            name="stare_num",
            field=models.IntegerField(default=18),
        ),
        migrations.AddField(
            model_name="csvdata",
            name="status",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="schema",
            name="separator",
            field=models.CharField(
                choices=[(",", "Comma"), (":", "Colon"), (";", "Semicolon")],
                default="'",
                max_length=2,
            ),
        ),
        migrations.AddField(
            model_name="schema",
            name="string_character",
            field=models.CharField(
                choices=[("'", "Single Quotes"), ('"', "Double Quotes")],
                default='"',
                max_length=2,
            ),
        ),
    ]

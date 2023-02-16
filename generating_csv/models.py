from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models


class User(AbstractUser):
    pass


class Column(models.Model):
    class ColumnsTypeChoices(models.TextChoices):
        FULL_NAME = "Full_name"
        JOB = "Job"
        EMAIL = "Email"
        PHONE_NUMBER = "Phone_number"
        ADDRESS = "Address"
        INTEGER = "Integer"

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=ColumnsTypeChoices.choices)
    order = models.IntegerField(unique=True, validators=[MinValueValidator(0)])

    def __str__(self):
        return f"Type: {self.type}, Name: {self.name}"


class Schema(models.Model):
    title = models.CharField(max_length=255)
    modified = models.TimeField(auto_now=True)
    columns = models.ManyToManyField(Column, related_name="schemas")

    def __str__(self):
        return f"Title: {self.title}, modified: {self.modified}"


class CSVData(models.Model):
    modified = models.TimeField(auto_now=True)
    schema = models.ForeignKey(Schema, on_delete=models.CASCADE)
    csv_file = models.URLField(max_length=255)
    rows = models.IntegerField(validators=[MinValueValidator(0)])

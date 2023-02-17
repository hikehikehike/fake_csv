from django import forms

from generating_csv.models import Schema, Column, CSVData


class SchemaForms(forms.ModelForm):
    class Meta:
        model = Schema
        fields = ["title", "columns"]

        widgets = {
            "columns": forms.HiddenInput(),
        }


class ColumnForms(forms.ModelForm):
    class Meta:
        model = Column
        fields = "__all__"


class CSVDataForms(forms.ModelForm):
    class Meta:
        model = CSVData
        fields = "__all__"

        widgets = {
            "schema": forms.HiddenInput(),
            "csv_file": forms.HiddenInput(),
        }

from django import forms

from generating_csv.models import Schema, Column, CSVData


class SchemaForms(forms.ModelForm):
    class Meta:
        model = Schema
        fields = ["title", "separator", "string_character", "columns"]

        widgets = {
            "columns": forms.HiddenInput(),
        }


class ColumnForms(forms.ModelForm):
    class Meta:
        model = Column
        fields = ["name", "type", "order", "start_num", "end_num"]


class CSVDataForms(forms.ModelForm):
    class Meta:
        model = CSVData
        fields = "__all__"

        widgets = {
            "schema": forms.HiddenInput(),
            "csv_file": forms.HiddenInput(),
            "status": forms.HiddenInput(),
        }

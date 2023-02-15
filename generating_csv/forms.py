from django import forms

from generating_csv.models import Schema, Column


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

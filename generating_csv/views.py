from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy, reverse

from generating_csv.forms import SchemaForms, ColumnForms
from generating_csv.models import Schema, Column


@login_required
def create_schema_and_columns(request):
    if request.method == "GET":
        column = Column.objects.all()
        context = {
            "schema_forms": SchemaForms(),
            "column_forms": ColumnForms(),
            "column": column,
        }
        return render(request, "generating_csv/schema_creation.html", context=context)

    if request.method == "POST":

        columns_form = ColumnForms(request.POST)
        if columns_form.is_valid():
            columns_form.save()
            return HttpResponseRedirect(reverse("generating_csv:schema-creation"))

        schema_form = SchemaForms(request.POST)
        if schema_form.is_valid():
            print("asd")
            schema_form.save()
            return HttpResponseRedirect(reverse("generating_csv:schema-list"))


class SchemaListViews(LoginRequiredMixin, generic.ListView):
    model = Schema
    fields = "__all__"


class SchemaDetailViews(LoginRequiredMixin, generic.DetailView):
    model = Schema
    fields = "__all__"


class SchemaUpdateViews(LoginRequiredMixin, generic.UpdateView):
    model = Schema
    fields = "__all__"
    success_url = reverse_lazy("generating_csv:schema-list")


class SchemaDeleteViews(LoginRequiredMixin, generic.DeleteView):
    model = Schema
    success_url = reverse_lazy("generating_csv:schema-list")




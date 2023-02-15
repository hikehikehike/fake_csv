from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from generating_csv.models import Schema


@login_required
def new_schema(request):
    return render(request, "tesdad.html")


class SchemaListViews(LoginRequiredMixin, generic.ListView):
    model = Schema
    fields = "__all__"

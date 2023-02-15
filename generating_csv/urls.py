from django.urls import path

from generating_csv.views import new_schema, SchemaListViews

urlpatterns = [
    path("", SchemaListViews.as_view(), name="schema-list"),
    path("new_schema/", new_schema, name="new-schema"),

]

app_name = "generating_csv"

from django.urls import path

from generating_csv.views import (
    SchemaListViews,
    SchemaUpdateViews,
    SchemaDeleteViews,
    create_schema_and_columns,
    ColumnsDeleteViews,
    create_csv_file,
)

urlpatterns = [
    path("", SchemaListViews.as_view(), name="schema-list"),
    path(
        "schema/creation/",
        create_schema_and_columns,
        name="schema-creation"
    ),
    path(
        "schema/<int:pk>/",
        create_csv_file,
        name="schema-detail"
    ),
    path(
        "schema/<int:pk>/update/",
        SchemaUpdateViews.as_view(),
        name="schema-update"
    ),
    path(
        "schema/<int:pk>/delete/",
        SchemaDeleteViews.as_view(),
        name="schema-delete"
    ),
    path(
        "columns/<int:pk>/delete/",
        ColumnsDeleteViews.as_view(),
        name="columns-delete"
    ),
]

app_name = "generating_csv"

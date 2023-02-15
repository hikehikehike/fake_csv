from django.contrib import admin

from generating_csv.models import User, Column, Schema

admin.site.register(User)
admin.site.register(Column)
admin.site.register(Schema)

from django.contrib import admin
from .models import Reuniao
from import_export.admin import ImportExportModelAdmin
from_encoding= 'utf-8-sig'


@admin.register(Reuniao)
class alunosadmin (ImportExportModelAdmin):
    list_display = ('name', 'serie', 'turma', 'ausente')
    list_filter = ("turma", "serie",)
    search_fields = ("name", "serie", "turma",)
    from_encoding = "utf-8-sig"





from django.contrib import admin
from .models import *


class GrupoAdmin(admin.ModelAdmin):
    filter_horizontal = ['pages', 'users']

admin.site.register(Page)
admin.site.register(Grupo, GrupoAdmin)
from django.contrib import admin
from .models import Hostage


class Hostage_admin(admin.ModelAdmin):
    list_display = ('name', 'info')


admin.site.register(Hostage, Hostage_admin)
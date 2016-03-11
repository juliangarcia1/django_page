from django.contrib import admin

# Register your models here.
from .models import Entrada


class EntradaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_creacion', 'fecha','estado')




admin.site.register(Entrada, EntradaAdmin)

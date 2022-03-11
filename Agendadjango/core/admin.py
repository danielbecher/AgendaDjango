from django.contrib import admin
from core.models import Evento

class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo','data_evento', 'data_criacao', 'id')
    list_filter = ('data_evento',)

admin.site.register(Evento, EventoAdmin)
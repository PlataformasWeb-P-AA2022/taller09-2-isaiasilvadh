from django.contrib import admin

from futbolec.models import Equipo, Jugador, Campeonato,CampeonatosEquipo

class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'siglas', 'twitter')
    search_fields = ('nombre', 'siglas')

admin.site.register(Equipo, EquipoAdmin)

admin.site.register(Jugador)
admin.site.register(Campeonato)


# admin.site.register(Matricula)
class CampeonatoEquipoAdmin(admin.ModelAdmin):

    list_display = ('anio', 'equipo', 'campeonato')
    search_fields = ('equipo__nombre', 'campeonato__nombre')

admin.site.register(CampeonatosEquipo, CampeonatoEquipoAdmin)
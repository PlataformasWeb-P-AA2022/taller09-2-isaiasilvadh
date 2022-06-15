from django.db import models

class Equipo(models.Model):

    nombre = models.CharField(max_length=30)
    siglas = models.CharField(max_length=30)
    twitter = models.CharField(max_length=30)
    campeonatos = models.ManyToManyField('Campeonato', through='CampeonatosEquipo')

    def __str__(self):
        return "Equipo = Nombre:%s - Siglas:%s - Twiter:%s" % (self.nombre, 
                self.siglas,
                self.twitter)


class Jugador(models.Model):
    nombre = models.CharField(max_length=30)
    posicion = models.CharField(max_length=30)
    numeroCamiseta = models.IntegerField('numero camiseta')
    sueldo = models.FloatField('sueldo')
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, \
            related_name="equipo")

    def __str__(self):
        return "Jugador = Nombre: %s - Posicion: %s - Numero de Camiseta: %d \
        sueldo: %d - Equipo(%s)" % (self.nombre, self.posicion, self.numeroCamiseta,
        self.sueldo, self.equipo)



class Campeonato(models.Model):

    nombre = models.CharField(max_length=30)
    auspiciante = models.CharField(max_length=30)

    equipos = models.ManyToManyField('Equipo', through='CampeonatosEquipo')

    def __str__(self):
        return "Campeonato = Nombre:%s - Auspiciante:%s" % (self.nombre, 
                self.auspiciante)


class CampeonatosEquipo(models.Model):
    anio = models.IntegerField('año')
    equipo = models.ForeignKey(Equipo, related_name='loscampeonatos', 
            on_delete=models.CASCADE)
    campeonato = models.ForeignKey(Campeonato, related_name='losequipos', 
            on_delete=models.CASCADE)

    def __str__(self):
        return "Campeonato: Año: %d - Equipo(%s) - Campeonato(%s)" % \
                (self.anio, self.equipo.nombre, self.campeonato.nombre)

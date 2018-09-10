# -*- encoding: utf-8 -*-
from django.test import TestCase

import datetime
from .models import *
from apps.trabajador.models import Veterinario
from apps.cliente.models import Cliente

class MascotaTestCase(TestCase):

    def setUp(self):

        veterinario = Veterinario.objects.create(dni='71205490', apellido= "apellidotestvet", nombre= "nombretestvet",
                               telefono= "telefonovet", fecha_contrato="2014-12-05",
                               especialidad="cardiologia")


        cliente = Cliente.objects.create(dni='71205489', apellido= "apellidotest", nombre= "nombretest",
                               telefono= "telefono",email="email@mail.com")

        mascota = Mascota.objects.create(nombre="mascotatestvet", cliente=cliente,
                                tipo="gato",raza="angora", tipo_alimento="casero",
                                fecha_nacimiento ="1995-04-01")

        cita = Cita.objects.create(veterinario=veterinario,
                                   mascota=mascota,
                                   fecha="2015-12-27")

        atencion = AtencionClinica.objects.create( veterinario= veterinario, mascota= mascota, fecha="2015-12-09",
                                                   diagnostico="diagnostico test",proxima_cita = cita)


    def test_creacion_cita(self):
        cita_encontrada = Cita.objects.filter(mascota__nombre="mascotatestvet", mascota__fecha_nacimiento="1995-04-01",
                                              fecha="2015-12-27")
        self.assertEqual(cita_encontrada[0].atendido, False)


    def test_creacion_atencion(self):

        atencion_encontrada = AtencionClinica.objects.filter(fecha="2015-12-09", mascota__nombre="mascotatestvet")
        self.assertEqual(atencion_encontrada[0].veterinario.nombre, 'nombretestvet')


    def test_programacion_cita(self):
        atencion_encontrada = AtencionClinica.objects.filter(fecha="2015-12-09", mascota__nombre="mascotatestvet")
        self.assertEqual(atencion_encontrada[0].proxima_cita.fecha, datetime.date(2015, 12, 27))









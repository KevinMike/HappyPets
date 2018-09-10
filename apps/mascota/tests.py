# -*- encoding: utf-8 -*-
from django.test import TestCase
from .models import Mascota
from apps.cliente.models import Cliente

# Create your tests here.

class MascotaTestCase(TestCase):

    def setUp(self):
        cliente = Cliente.objects.create(dni='71205489', apellido= "apellidotest", nombre= "nombretest",
                               telefono= "telefono",email="email@mail.com")
        mascota = Mascota.objects.create(nombre="mascotatest", cliente=cliente,
                                tipo="gato",raza="angora", tipo_alimento="casero",
                                fecha_nacimiento ="1995-04-01")


    def test_creacion_mascota(self):
        mascota_encontrada = Mascota.objects.filter(fecha_nacimiento="1995-04-01", nombre="mascotatest")
        self.assertEqual(mascota_encontrada[0].raza, 'angora')
        self.assertEqual(mascota_encontrada[0].tipo, 'gato')

    def test_mascotas_tienen_dueno(self):

        mascota_encontrada = Mascota.objects.get(fecha_nacimiento="1995-04-01", nombre="mascotatest")
        self.assertEqual(mascota_encontrada.cliente.nombre, 'nombretest')
        self.assertEqual(mascota_encontrada.cliente.email, 'email@mail.com')



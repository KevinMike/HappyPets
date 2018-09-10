# -*- encoding: utf-8 -*-
from django.test import TestCase
from apps.mascota.models import Mascota
from .models import Cliente

class MascotaTestCase(TestCase):
    def setUp(self):
        pass

    def test_creacion_cliente(self):
        cliente = Cliente.objects.create(dni='71205489', apellido= "apellidotest", nombre= "nombretest",
                               telefono= "telefono",email="email@mail.com")
        self.assertEqual(cliente.nombre, 'nombretest')
        self.assertEqual(cliente.dni, '71205489')
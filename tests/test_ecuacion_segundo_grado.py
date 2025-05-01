import unittest
from src.logica.ecuacion_segundo_grado import EcuacionSegundoGrado

class TestEcuacionSegundoGrado(unittest.TestCase):

    def test_solucionESG_parametrosNumericos_raicesReales(self):
        # Arrange (Preparar los datos de entrada)
        ecuacion = EcuacionSegundoGrado()
        ecuacion.a = 3
        ecuacion.b = -5
        ecuacion.c = 1

        # Valores esperados
        RaizEsperada1 = 1.43
        RaizEsperada2 = 0.23

        # Act (Llamar a la función)
        RaizActual1, RaizActual2 = ecuacion.solucionESG()

        # Assert (Comparar resultado)
        self.assertAlmostEqual(RaizEsperada1, RaizActual1, 2)
        self.assertAlmostEqual(RaizEsperada2, RaizActual2, 2)

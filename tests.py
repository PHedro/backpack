import unittest

from mensalidades.main import recupera_indice_faturas, recupera_indice_faturas_amortizado


class MyTestCase(unittest.TestCase):
    def test_recupera_indice_faturas(self):
        mensalidades = [300, 700, 2000]
        target = 2300
        result = recupera_indice_faturas(mensalidades, target)
        self.assertEqual((0, 2), result)

    def test_recupera_indice_faturas_2(self):
        mensalidades = [300, 700, 2000]
        target = 2700
        result = recupera_indice_faturas(mensalidades, target)
        self.assertEqual((1, 2), result)

    def test_recupera_indice_faturas_3(self):
        mensalidades = [300, 700, 700, 2000]
        target = 1400
        result = recupera_indice_faturas(mensalidades, target)
        self.assertEqual((1, 2), result)

    def test_recupera_indice_faturas_4(self):
        mensalidades = [300, 2000]
        target = 2300
        result = recupera_indice_faturas(mensalidades, target)
        self.assertEqual((0, 1), result)

    def test_recupera_indice_faturas_amortizado(self):
        mensalidades = [300, 700, 2000]
        target = 2300
        result = recupera_indice_faturas_amortizado(mensalidades, target)
        self.assertEqual([0, 2], result)

    def test_recupera_indice_faturas_amortizado_2(self):
        mensalidades = [300, 700, 2000]
        target = 2700
        result = recupera_indice_faturas_amortizado(mensalidades, target)
        self.assertEqual([1, 2], result)

    def test_recupera_indice_faturas_amortizado_3(self):
        mensalidades = [300, 700, 700, 2000]
        target = 1400
        result = recupera_indice_faturas_amortizado(mensalidades, target)
        self.assertEqual([1, 2], result)

    def test_recupera_indice_faturas_amortizado_4(self):
        mensalidades = [300, 2000]
        target = 2300
        result = recupera_indice_faturas_amortizado(mensalidades, target)
        self.assertEqual([0, 1], result)

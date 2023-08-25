import unittest
from highestAndLowest import high_and_low

class TestHighestAndLowest(unittest.TestCase):
    
    def test_receber_numeros_em_strings_espaçadas_e_retornar_maior_menor_valor(self):
        entradas_e_saidas = [
            ('8 3 -5 42 -1 0 0 -9 4 7 4 -4', '42 -9'),
            ('1 2 3', '3 1')
        ]

        for entrada, saida in entradas_e_saidas:
            with self.subTest(entrada = entrada, saida = saida):
                self.assertEqual(high_and_low(entrada), saida)

if __name__ == '__main__':
    unittest.main(verbosity=2)
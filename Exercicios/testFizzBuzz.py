import unittest
from fizzBuzz import fizzBuzz

class TestFizzBuzz(unittest.TestCase):

    def test_deve_retornar_FizzBuzz_se_entrada_multiplo_de_3_e_5(self):
        entradas = (15, 30, 45, 60)

        for entrada in entradas:
            with self.subTest(entrada = entrada):
                self.assertEqual(fizzBuzz(entrada), "FizzBuzz")
    
    def test_deve_retornar_Fizz_se_entrada_multiplo_de_3_nao_5(self):
        entradas = (3, 6, 9, 12, 18)

        for entrada in entradas:
            with self.subTest(entrada = entrada):
                self.assertEqual(fizzBuzz(entrada), "Fizz")

    def test_deve_retornar_Buzz_se_entrada_multiplo_de_5_nao_3(self):
        entradas = (5, 10, 20, 25, 35)
        
        for entrada in entradas:
            with self.subTest(entrada = entrada):
                self.assertEqual(fizzBuzz(entrada), "Buzz")

    def teste_deve_retornar_n_se_entrada_de_n_não_for_multiplo_de_3e_ou5(self):
        entradas = (1, 11, 13, 16, 19)
        
        for entrada in entradas:
            with self.subTest(entrada = entrada):
                self.assertEqual(fizzBuzz(entrada), entrada)

if __name__ == '__main__':
    unittest.main(verbosity=2)
        
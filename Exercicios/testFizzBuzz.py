import unittest
from fizzBuzz import fizzBuzz

class TestFizzBuzz(unittest.TestCase):

    def test_deve_retornar_FizzBuzz_se_entrada_multiplo_de_3_e_5(self):
        esperado = [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']
        self.assertEqual(fizzBuzz(15), esperado)

    def test_deve_ret(self):
        ...

if __name__ == '__main__':
    unittest.main()
        
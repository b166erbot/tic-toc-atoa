from unittest import TestCase
from src.tic_tac_toe import numerar


class Tests(TestCase):
    forma = '\x1b[38;5;245m {}\x1b[0m'

    def test_retornando_uma_lista_com_strings(self):
        resultado = numerar([' '] * 9)
        self.assertTrue(all(map(lambda x: isinstance(x, str), resultado)))

    def test_retornando_todos_os_numeros_caso_so_haja_espaco(self):
        resultado = numerar([' '] * 9)
        esperado = list(map(self.forma.format, range(1, 10)))
        self.assertEqual(resultado, esperado)

    def test_retornando_numeros_onde_contenha_espaco(self):
        resultado = numerar([' '] * 5 + ['X'] * 5)
        temp = list(map(self.forma.format, ['1', '2', '3', '4', '5']))
        esperado = temp + ['X'] * 5
        self.assertEqual(resultado, esperado)

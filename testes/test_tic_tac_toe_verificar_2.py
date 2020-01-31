from unittest import TestCase

from src.tic_tac_toe import verificar_2


class Testes(TestCase):
    def test_retornando_False_caso_lista_nao_bata_no_padao_1(self):
        lista = ['X  ', ' X ', '   ']
        resultado, esperado = verificar_2(lista), False
        self.assertEqual(resultado, esperado)

    def test_retornando_False_caso_lista_nao_bata_no_padao_2(self):
        lista = ['X  ', '   ', '  X']
        resultado, esperado = verificar_2(lista), False
        self.assertEqual(resultado, esperado)

    def test_retornando_False_caso_lista_nao_bata_no_padao_3(self):
        lista = ['   ', ' X ', '  X']
        resultado, esperado = verificar_2(lista), False
        self.assertEqual(resultado, esperado)

    def test_retornando_False_caso_lista_nao_bata_no_padao_4(self):
        lista = ['   ', ' X ', 'X  ']
        resultado, esperado = verificar_2(lista), False
        self.assertEqual(resultado, esperado)

    def test_retornando_False_caso_lista_nao_bata_no_padao_5(self):
        lista = ['  X', '   ', 'X  ']
        resultado, esperado = verificar_2(lista), False
        self.assertEqual(resultado, esperado)

    def test_retornando_False_caso_lista_nao_bata_no_padao_6(self):
        lista = ['  X', ' X ', '   ']
        resultado, esperado = verificar_2(lista), False
        self.assertEqual(resultado, esperado)

    def test_retornando_x_caso_lista_bata_no_padrao_1(self):
        lista = ['  X', ' X ', 'X  ']
        resultado, esperado = verificar_2(lista), 'X'
        self.assertEqual(resultado, esperado)

    def test_retornando_x_caso_lista_bata_no_padrao_2(self):
        lista = ['X  ', ' X ', '  X']
        resultado, esperado = verificar_2(lista), 'X'
        self.assertEqual(resultado, esperado)

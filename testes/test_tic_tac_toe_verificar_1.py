from unittest import TestCase
from src.tic_tac_toe import verificar_1


class Testes(TestCase):
    def test_retornando_False_caso_alguma_fileira_venca(self):
        lista = [range(3), range(3)[::-1], range(3, 7)]
        resultado, esperado = verificar_1(lista), False
        self.assertEqual(resultado, esperado)

    def test_retornando_x_caso_o_x_venca_na_primeira_fileira(self):
        lista = [['X'] * 3, range(3), range(3)]
        resultado, esperado = verificar_1(lista), 'X'
        self.assertEqual(resultado, esperado)

    def test_retornando_x_caso_o_x_venca_na_segunda_fileira(self):
        lista = [range(3), ['X'] * 3, range(3)]
        resultado, esperado = verificar_1(lista), 'X'
        self.assertEqual(resultado, esperado)

    def test_retornando_x_caso_o_x_venca_na_terceira_fileira(self):
        lista = [range(3), range(3), ['X'] * 3]
        resultado, esperado = verificar_1(lista), 'X'
        self.assertEqual(resultado, esperado)

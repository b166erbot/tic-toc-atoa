from unittest import TestCase

from src.tic_tac_toe import vencedor


class Testes(TestCase):
    dicio = {'usuário': 'X', 'máquina': 'O', False: False}

    def test_retornando_False_caso_lista_nao_bata_no_padrao_1(self):
        lista = [1, 2, 3, 3, 2, 1, 2, 3, ' ']
        resultado, esperado = vencedor(self.dicio, lista), False
        self.assertEqual(resultado, esperado)

    def test_retornando_usuario_caso_o_x_venca(self):
        lista = ['X', 'X', 'X', 1, 2, 3, 1, 2, 3]
        resultado, esperado = vencedor(self.dicio, lista), 'usuário'
        self.assertEqual(resultado, esperado)

    def test_retornando_usuario_caso_o_O_venca(self):
        lista = ['O', 'O', 'O', 1, 2, 3, 1, 2, 3]
        resultado, esperado = vencedor(self.dicio, lista), 'máquina'
        self.assertEqual(resultado, esperado)

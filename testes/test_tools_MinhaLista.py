from unittest import TestCase, skip
from src.tools import MinhaLista
from typing import Iterator, Iterable


class Testes(TestCase):
    def setUp(self):
        self.lista = MinhaLista([' '] * 9 + ['X'])

    def test_retornando_uma_lista_iterable_caso_MinhaLista_seja_iterado(self):
        self.assertIsInstance(self.lista.__iter__(), Iterator)

    def test_vazios_retornando_todos_os_itens_nao_alterados_da_MinhaLista(self):
        resultado, esperado = self.lista.vazios(), [*range(9)]
        self.assertEqual(resultado, esperado)

    def test_setitem_definindo_True_caso_posicao_1_seja_escolhido(self):
        self.lista[1] = 'X'
        self.assertEqual(self.lista.posicoes[1], True)

    def test_setitem_nao_definindo_O_na_lista_caso_posicao_ja_alterada(self):
        self.lista[1] = 'X'
        self.lista[1] = 'O'
        self.assertEqual(self.lista[1], 'X')

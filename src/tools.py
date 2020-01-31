"""Módulo de ferramentas para o tic_tac_toe."""


from typing import Any, Iterator, List, NoReturn


class MinhaLista:
    """Uma lista que altera somente uma vez o item com o __setitem__."""

    def __init__(self, lista: list) -> NoReturn:
        """Método inicializador."""
        self.lista = list(lista)
        self.posicoes = [False] * len(lista)

    def __setitem__(self, posicao: int, item: str) -> NoReturn:
        """Método que só define um atributo uma vez."""
        if not self.posicoes[posicao]:
            self.lista[posicao] = item
            self.posicoes[posicao] = True

    def __getitem__(self, posicao: int) -> Any:
        """Método que exibe um item em uma posição específica."""
        return self.lista[posicao]

    def __iter__(self) -> Iterator[Any]:
        """Método que retorna uma lista iteradora caso o objeto seja iterado."""
        return iter(self.lista)

    def vazios(self) -> List[int]:
        """Método que retorna uma lista com todos os espaços vazios."""
        temp = filter(lambda x: x[1] == ' ', enumerate(self.lista, 1))
        return list(map(lambda x: str(x[0]), temp))

    def __repr__(self) -> str:
        """Método que retorna uma string como representação do objeto."""
        return f"MinhaLista: {self.lista}"

    def __len__(self) -> int:
        """Método que retorna o tamanho total da lista neste objeto."""
        return len(self.lista)

    def __contains__(self, valor: Any) -> bool:
        """Método que revela se algum item contém dentro desta lista."""
        return valor in self.lista

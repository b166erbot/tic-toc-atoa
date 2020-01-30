from typing import NoReturn, Iterator, Any, List


class MinhaLista:
    """ Uma lista que altera somente uma vez o item com o __setitem__. """
    def __init__(self, lista: list) -> NoReturn:
        self.lista = list(lista)
        self.posicoes = [False] * len(lista)

    def __setitem__(self, posicao: int, item: str) -> NoReturn:
        if not self.posicoes[posicao]:
            self.lista[posicao] = item
            self.posicoes[posicao] = True

    def __getitem__(self, posicao: int) -> Any:
        return self.lista[posicao]

    def __iter__(self) -> Iterator[Any]:
        return iter(self.lista)

    def vazios(self) -> List[int]:
        temp = filter(lambda x: x[1] == ' ', enumerate(self.lista, 1))
        return list(map(lambda x: str(x[0]), temp))

    def __repr__(self) -> str:
        return f"MinhaLista: {self.lista}"

    def __len__(self) -> int:
        return len(self.lista)

    def __contains__(self, valor: Any) -> bool:
        return valor in self.lista

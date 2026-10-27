from aula09_estudo_fila import FilaPaises  # type: ignore[reportMissingImports]

class FilaPaisesEstudo(FilaPaises):
    def __init__(self):
        super().__init__()

    def adicionar_pais(self, pais):
        self.enfileirar(pais)

    def remover_pais(self):
        return self.desenfileirar()

    def listar_paises(self):
        print("Tamanho da fila de países: ", self.tamanho())
        if self.inicio() is not None:
            print("País no início da fila:", self.inicio().dado)
        else:
            print("A fila está vazia.")
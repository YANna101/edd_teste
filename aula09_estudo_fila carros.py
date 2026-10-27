from aula09_estudo_fila import FilaCarros  # type: ignore[reportMissingImports]
class FilaCarrosEstudo(FilaCarros):
    def __init__(self):
        super().__init__()

    def adicionar_carro(self, carro):
        self.enfileirar(carro)

    def remover_carro(self):
        return self.desenfileirar()

    def listar_carros(self):
        print("Tamanho da fila de carros: ", self.tamanho())
        if self.inicio() is not None:
            print("Carro no início da fila:", self.inicio().dado)
        else:
            print("A fila está vazia.")
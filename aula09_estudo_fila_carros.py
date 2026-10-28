from aula09_fila import fila
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
            
       
       if __name__ == "__main__":
    fila_carros_exemplo = FilaCarrosEstudo()
    fila_carros_exemplo.adicionar_carro("Carro A")
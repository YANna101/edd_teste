from aula09_fila import Fila

class FilaCompras:
    def __init__(self):
        self.fila = Fila()

    def adicionar_item(self, item):
        self.fila.enfileirar(item)

    def remover_item(self):
        return self.fila.desenfileirar().dado

    def listar_itens(self):
        self.fila.listar_fila()
        print("Tamanho da fila de compras:", self.fila.tamanho())
        print("Item no início da fila:", self.fila.inicio().dado)
        if __name__ == "__main__":
            # Testando a fila de compras
            fila_compras_exemplo = FilaCompras()
            fila_compras_exemplo.adicionar_item("Maçã")
            fila_compras_exemplo.adicionar_item("Banana")
            fila_compras_exemplo.adicionar_item("Laranja")
            fila_compras_exemplo.listar_itens()

            print("Removendo item:", fila_compras_exemplo.remover_item())
            fila_compras_exemplo.listar_itens()
            
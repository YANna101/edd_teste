from no import No
from edd.aula11_lista_ligada import ListaLigada

class ListaCompras(ListaLigada):
    def __init__(self,produto):
        super().__init__()
        self.produto = produto
    def adicionar_item(self, item):
        self.adicionar(item)

    def remover_item(self, item):
        self.remover(item)

    def exibir_lista(self):
        self.exibir()
        
if __name__ == "__main__":
    lista_compras = ListaCompras()
    lista_compras.adicionar_item("Arroz")
    lista_compras.adicionar_item("Feijão")
    lista_compras.adicionar_item("Macarrão")
    lista_compras.exibir_lista()
    lista_compras.remover_item("Feijão")
    lista_compras.exibir_lista()
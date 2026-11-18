# from no import No
from aula11_lista_ligada_ordenada import ListaLigadaOrdenada

class ListaCompras(ListaLigadaOrdenada):
    def __init__(self):
        super().__init__()
    def adicionar_item(self, item):
        self.inserir(item)

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
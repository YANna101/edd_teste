from edd.aula11_lista_ligada import ListaLigada
from no import No

class ListaFlores(ListaLigada):
    def __init__(self):
        super().__init__()

    def adicionar_flor(self, flor):
        self.adicionar(flor)

    def remover_flor(self, flor):
        self.remover(flor)

    def exibir_lista(self):
        self.exibir()

if __name__ == "__main__":
    lista_flores = ListaFlores()
    lista_flores.adicionar_flor("Rosa")
    lista_flores.adicionar_flor("Tulipa")
    lista_flores.adicionar_flor("Girassol")
    lista_flores.exibir_lista()
    lista_flores.remover_flor("Tulipa")
    lista_flores.exibir_lista()
    

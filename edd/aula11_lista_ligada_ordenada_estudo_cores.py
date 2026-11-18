from aula11_lista_ligada_ordenada import ListaLigadaOrdenada
# from no import No

class ListaCores(ListaLigadaOrdenada):
    def __init__(self):
        super().__init__()

    def adicionar_cor(self, cor):
        # self.adicionar(cor)
        self.inserir(cor)

    def remover_cor(self, cor):
        self.remover(cor)

    def exibir_lista(self):
        self.exibir()
        
if __name__ == "__main__":
    lista_cores = ListaCores()
    lista_cores.adicionar_cor("Vermelho")
    lista_cores.adicionar_cor("Verde")
    lista_cores.adicionar_cor("Azul")
    lista_cores.exibir_lista()
    lista_cores.remover_cor("Verde")
    lista_cores.exibir_lista()
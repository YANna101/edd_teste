from aula08_pilha import Pilha

class PilhaFlores:
    def __init__(self):
        self.pilha = Pilha()

    def adicionar_flor(self, flor):
        self.pilha.empilhar(flor)

    def remover_flor(self):
        return self.pilha.desempilhar().dado

    def listar_flores(self):
        self.pilha.listar_pilha()
        print("Tamanho da pilha de flores:", self.pilha.tamanho())
        print("Flor no topo da pilha:", self.pilha.topo().dado)
if __name__ == "__main__":
    # Testando a pilha de flores
    pilha_flores_exemplo = PilhaFlores()
    pilha_flores_exemplo.adicionar_flor("Rosa")
    pilha_flores_exemplo.adicionar_flor("Tulipa")
    pilha_flores_exemplo.adicionar_flor("Girassol")
    pilha_flores_exemplo.listar_flores()
    
    print("Removendo flor:", pilha_flores_exemplo.remover_flor())
    pilha_flores_exemplo.listar_flores()
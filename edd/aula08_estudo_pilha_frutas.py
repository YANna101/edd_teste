from aula08_pilha import Pilha

# exemplo de uso da pilha
# conversão de frutas em uma pilha
class PilhaFrutas:
    def __init__(self):
        self.pilha = Pilha()

    def adicionar_fruta(self, fruta):
        self.pilha.empilhar(fruta)

    def remover_fruta(self):
        return self.pilha.desempilhar().dado

    def listar_frutas(self):
        self.pilha.listar_pilha()
        print("Tamanho da pilha de frutas:", self.pilha.tamanho())
        print("Frutas no topo da pilha:", self.pilha.topo().dado)
        
        
if __name__ == "__main__":
    # Testando a pilha de frutas
    pilha_frutas_exemplo = PilhaFrutas()
    pilha_frutas_exemplo.adicionar_fruta("Maçã")
    pilha_frutas_exemplo.adicionar_fruta("Banana")
    pilha_frutas_exemplo.adicionar_fruta("Laranja")
    pilha_frutas_exemplo.listar_frutas()
    
    print("Removendo fruta:", pilha_frutas_exemplo.remover_fruta())
    pilha_frutas_exemplo.listar_frutas()
from aula08_pilha import Pilha

# exemplo 4 cores pilha
class PilhaCores:
    def __init__(self):
        self.pilha = Pilha()

    def adicionar_cor(self, cor):
        self.pilha.empilhar(cor)

    def remover_cor(self):
        return self.pilha.desempilhar().dado

    def listar_cores(self):
        self.pilha.listar_pilha()
        print("Tamanho da pilha de cores:", self.pilha.tamanho())
        print("Cor no topo da pilha:", self.pilha.topo().dado)
    

if __name__ == "__main__":
    # Testando a pilha de cores
    pilha_cores_exemplo = PilhaCores()
    pilha_cores_exemplo.adicionar_cor("Vermelho")
    pilha_cores_exemplo.adicionar_cor("Verde")
    pilha_cores_exemplo.adicionar_cor("Azul")
    pilha_cores_exemplo.listar_cores()
    
    print("Removendo cor:", pilha_cores_exemplo.remover_cor())
    pilha_cores_exemplo.listar_cores()
from aula08_pilha import Pilha
        
        # pilha 2 números
class PilhaNumeros:
    def __init__(self):
        self.pilha = Pilha()

    def adicionar_numero(self, numero):
        self.pilha.empilhar(numero)

    def remover_numero(self):
        return self.pilha.desempilhar().dado

    def listar_numeros(self):
        self.pilha.listar_pilha()
        print("Tamanho da pilha de números:", self.pilha.tamanho())
        print("Número no topo da pilha:", self.pilha.topo().dado)
    
if __name__ == "__main__":
    # Testando a pilha de números
    pilha_numeros_exemplo = PilhaNumeros()
    pilha_numeros_exemplo.adicionar_numero(1)
    pilha_numeros_exemplo.adicionar_numero(2)
    pilha_numeros_exemplo.adicionar_numero(3)
    pilha_numeros_exemplo.listar_numeros()
    
    print("Removendo número:", pilha_numeros_exemplo.remover_numero())
    pilha_numeros_exemplo.listar_numeros()
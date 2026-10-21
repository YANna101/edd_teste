from __future__ import annotations
from no import No

# exemplo do meu professor de como implementar uma pilha usando uma lista encadeada
class Pilha:
    def __init__(self) -> Pilha:
        self._topo = None
        self._tamanho = 0

    def esta_vazia(self) -> bool: # is_empty
        return self._topo is None

    def empilhar(self, item) -> None: # push
        if self.esta_vazia():
            self._topo = No(item)
        else:
            novo_no = No(item, self._topo)
            self._topo = novo_no
        self._tamanho += 1

    def desempilhar(self) -> No: # pop
        if self.esta_vazia():
            raise IndexError("A pilha está vazia.")
        else:
            no_removido = self._topo
            self._topo = self._topo.prox
            self._tamanho -= 1
            return no_removido
        
    def topo(self) -> No: # peek
        if self.esta_vazia():
            raise IndexError("A pilha está vazia.")
        else:
            return self._topo
        
    def tamanho(self) -> int: # size
        return self._tamanho
    
    def listar_pilha(self) -> None: # list_stack
        if self.esta_vazia():
            print("A pilha está vazia.")
        else:
            print("Elementos da pilha:")
            print("\tTOPO")
            no_atual = self._topo
            while no_atual is not None:
                print(no_atual.dado)
                no_atual = no_atual.prox
            print("\tFUNDO")
            
            
if __name__ == "__main__":
    pilha = Pilha()
    pilha.empilhar(10)
    pilha.empilhar(20)
    pilha.empilhar(30)
    pilha.listar_pilha()
    
    print("Desempilhando:", pilha.desempilhar().dado)
    pilha.listar_pilha()
    
    print("Topo da pilha:", pilha.topo().dado)
    print("Tamanho da pilha:", pilha.tamanho())


# minhas pilhas de frutas e números usando a pilha do professor pilha 1 frutas 

# exemplo de uso da pilha
# conversão de frutas em uma pilha
class pilha_frutas:
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
        
        
        
        
        # pilha 2 números
class pilha_numeros:
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
    

# exemplo teste de uso das pilhas de frutas e números pilha 3
if __name__ == "__main__":
    # Testando a pilha de frutas
    pilha_frutas_exemplo = pilha_frutas()
    pilha_frutas_exemplo.adicionar_fruta("Maçã")
    pilha_frutas_exemplo.adicionar_fruta("Banana")
    pilha_frutas_exemplo.adicionar_fruta("Laranja")
    pilha_frutas_exemplo.listar_frutas()
    
    print("Removendo fruta:", pilha_frutas_exemplo.remover_fruta())
    pilha_frutas_exemplo.listar_frutas()
    
    # Testando a pilha de números
    pilha_numeros_exemplo = pilha_numeros()
    pilha_numeros_exemplo.adicionar_numero(1)
    pilha_numeros_exemplo.adicionar_numero(2)
    pilha_numeros_exemplo.adicionar_numero(3)
    pilha_numeros_exemplo.listar_numeros()
    
    print("Removendo número:", pilha_numeros_exemplo.remover_numero())
    pilha_numeros_exemplo.listar_numeros()
    
    
    
    
    
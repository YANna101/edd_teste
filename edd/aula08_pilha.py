from __future__ import annotations
from no import No


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



# exemplo de uso da pilha
# cosvesão de frutas em uma pilha
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
        print("futas no topo da pilha:", self.pilha.topo().dado)
    


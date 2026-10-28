from __future__ import annotations
from no import No

class Fila: 
    def __init__(self) -> Fila:
        self._inicio = None
        self._fim = None
        self._tamanho = 0
        
        
    @property
    def inicio(self) -> No: # get_start
        return self._inicio
    
    @inicio.setter
    def inicio(self, no: No) -> None: # set_start
        self._inicio = no

    @property
    def fim(self) -> No: # get_end
        return self._fim

    @fim.setter
    def fim(self, no: No) -> None: # set_end
        self._fim = no

    def esta_vazia(self) -> bool: # is_empty
        return self.inicio is None

    def enfileirar(self, item) -> None: # put ou enqueue
        novo_no = No(item)
        if self.esta_vazia(): # situação 01
            self.inicio = novo_no
            self.fim = novo_no
        else: # situação 02
            self.fim.prox = novo_no
            self.fim = novo_no
        self._tamanho += 1

    def desenfileirar(self) -> No: # remove ou dequeue
        if self.esta_vazia():
            raise IndexError("A fila está vazia.")
        else:
            no_removido = self.inicio
            self.inicio = self.inicio.prox
            if self.inicio is None:
                self.fim = None
            self._tamanho -= 1
    
            # print(f"Desenfileirando: {no_removido.dado}")

            return no_removido
   
        
    def consultar_inicio(self) -> No: # get ou peek
        if self.esta_vazia():
            raise IndexError("A fila está vazia.")
        else:
            return self.inicio
        
    def tamanho(self) -> int: # size
        return self._tamanho
    
    def listar_fila(self) -> None: # list_queue
        if self.esta_vazia():
            print("A fila está vazia.")
        else:
            print("Elementos da fila:")
            no_atual = self.inicio
            while no_atual is not None:
                print(no_atual.dado)
                no_atual = no_atual.prox
                
    
if __name__ == "__main__":
    fila = Fila()
    fila.enfileirar(10)
    fila.enfileirar(20)
    fila.enfileirar(30)
    fila.listar_fila()
    
    print("Desenfileirando:", fila.desenfileirar().dado)
    fila.listar_fila()
    
    print("Início da fila:", fila.consultar_inicio().dado)
    print("Tamanho da fila:", fila.tamanho())
        
    fila.desenfileirar()
    fila.desenfileirar()
    fila.listar_fila()
    
    try:
        fila.desenfileirar()  # Tentativa de desenfileirar de uma fila vazia
    except IndexError as e:
        print("Erro:", e)
        

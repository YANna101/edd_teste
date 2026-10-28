from collections import deque as Fila

class Filapaises:
    def __init__(self):
        self.fila = Fila()

    def adicionar_pais(self, pais):
        self.fila.append(pais)

    def remover_pais(self):
        if not self.esta_vazia():
            return self.fila.popleft()
        else:
            raise IndexError("A fila de países está vazia.")

    def listar_paises(self):
        print("Tamanho da fila de países: ", len(self.fila))
        if not self.esta_vazia():
            print("País no início da fila:", self.fila[0])
        else:
            print("A fila de países está vazia.")

    def esta_vazia(self):
        return len(self.fila) == 0
    
if __name__ == "__main__":
    fila_paises_exemplo = Filapaises()
    fila_paises_exemplo.adicionar_pais("Brasil")
    fila_paises_exemplo.adicionar_pais("Argentina")
    fila_paises_exemplo.adicionar_pais("Chile")
    fila_paises_exemplo.listar_paises()

    print("Removendo país:", fila_paises_exemplo.remover_pais())
    fila_paises_exemplo.listar_paises()
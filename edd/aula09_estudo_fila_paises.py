from aula09_fila import Fila


class Pais:
    def __init__(self, nome, populacao):
        self.nome = nome
        self.populacao = populacao

    def __str__(self):
        return f"{self.nome} - População: {self.populacao}"

class FilaPaises:
    def __init__(self):
        self.fila = Fila()

    def adicionar_pais(self, pais):
        self.fila.enfileirar(pais)

    def remover_pais(self):
        if not self.fila.esta_vazia():
            return self.fila.desenfileirar().dado
        else:
            raise IndexError("A fila de países está vazia.")

    def listar_paises(self):
        print("Tamanho da fila de países: ", self.fila.tamanho())
        if not self.fila.esta_vazia():
            self.fila.listar_fila()
        else:
            print("A fila de países está vazia.")

    
    
    
if __name__ == "__main__":
    fila_paises_exemplo = FilaPaises()
    
    pais1 = Pais("Brasil", 213000000)
    pais2 = Pais("Argentina", 45000000)
    pais3 = Pais("Chile", 19000000)
    pais4 = Pais("Peru", 33000000)
    pais5 = Pais("Colômbia", 51000000)
    
    fila_paises_exemplo.adicionar_pais(pais1)
    fila_paises_exemplo.adicionar_pais(pais2)
    fila_paises_exemplo.adicionar_pais(pais3)
    fila_paises_exemplo.adicionar_pais(pais4)
    fila_paises_exemplo.adicionar_pais(pais5)
    fila_paises_exemplo.listar_paises()

    print(f"Removendo país: {fila_paises_exemplo.remover_pais()}")
    fila_paises_exemplo.listar_paises()
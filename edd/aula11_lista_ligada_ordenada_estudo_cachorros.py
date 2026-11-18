from no import No
from aula11_lista_ligada_ordenada import ListaLigadaOrdenada

class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"{self.nome} ({self.idade} anos)"
    
    
    def __lt__(self, other):
        return self.idade < other.idade
    
    
    def __gt__(self, other):
        return self.idade > other.idade
    
    
    def __eq__(self, other):
        return self.idade == other.idade and self.nome == other.nome
    


class ListaCachorros(ListaLigadaOrdenada):
    def __init__(self):
        super().__init__()

    def adicionar_cachorro(self, nome, idade):
        cachorro = No(Cachorro(nome, idade))
        self.inserir(cachorro)

    def listar_cachorros(self):
        self.exibir()
        # for cachorro in self:
        #     print(f"Nome: {cachorro.dado.nome}, Idade: {cachorro.dado.idade} anos")
            
        #     if cachorro.proximo is not None:
        #         print("->", end=" ")
                
if __name__ == "__main__":
    lista_cachorros = ListaCachorros()
    lista_cachorros.adicionar_cachorro("Rex", 3)
    lista_cachorros.adicionar_cachorro("Luna", 2)
    lista_cachorros.adicionar_cachorro("Max", 5)
    lista_cachorros.listar_cachorros()   
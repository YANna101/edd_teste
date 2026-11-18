from no import No
from edd.aula11_lista_ligada import ListaLigada


class cahorros(ListaLigada):
    def __init__(self):
        super().__init__()

    def adicionar_cachorro(self, nome, idade):
        cachorro = No((nome, idade))
        self.adicionar(cachorro)

    def listar_cachorros(self):
        for cachorro in self:
            print(f"Nome: {cachorro.dado[0]}, Idade: {cachorro.dado[1]} anos")
            
            if cachorro.proximo is not None:
                print("->", end=" ")
                
        if __name__ == "__main__":
         lista_cachorros = cahorros()
         lista_cachorros.adicionar_cachorro("Rex", 3)
         lista_cachorros.adicionar_cachorro("Luna", 2)
        lista_cachorros.adicionar_cachorro("Max", 5)
        lista_cachorros.listar_cachorros()   
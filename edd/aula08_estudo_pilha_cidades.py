from aula08_pilha import Pilha
class PilhaCidades:
    def __init__(self):
        self.pilha = Pilha()

    def adicionar_cidade(self, cidade):
        self.pilha.empilhar(cidade)

    def remover_cidade(self):
        return self.pilha.desempilhar().dado

    def listar_cidades(self):
        self.pilha.listar_pilha()
        print("Tamanho da pilha de cidades:", self.pilha.tamanho())
        print("Cidade no topo da pilha:", self.pilha.topo().dado)
if __name__ == "__main__":
    # Testando a pilha de cidades
    pilha_cidades_exemplo = PilhaCidades()
    pilha_cidades_exemplo.adicionar_cidade("São Paulo")
    pilha_cidades_exemplo.adicionar_cidade("Rio de Janeiro")
    pilha_cidades_exemplo.adicionar_cidade("Belo Horizonte")
    pilha_cidades_exemplo.listar_cidades()
    
    print("Removendo cidade:", pilha_cidades_exemplo.remover_cidade())
    pilha_cidades_exemplo.listar_cidades()
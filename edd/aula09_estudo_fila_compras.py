from aula09_fila import Fila

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} - Preço: R${self.preco:.2f}"


class FilaCompras:
    def __init__(self):
        self.fila = Fila()

    def adicionar_item(self, item):
        self.fila.enfileirar(item)

    def remover_item(self):
        return self.fila.desenfileirar().dado

    def listar_itens(self):
        print("Tamanho da fila de compras: ", self.fila.tamanho())
        print("Item no início da fila:", self.fila.inicio.dado)

# Mova este bloco totalmente para a esquerda (sem espaços no início)
if __name__ == "__main__":
    # Deixe apenas 4 espaços de recuo para o código abaixo:
    fila_compras_exemplo = FilaCompras()
    
    produto1 = Produto("Maçã", 3.50)
    produto2 = Produto("Banana", 2.00)
    produto3 = Produto("Laranja", 4.00)
    produto4 = Produto("Uva", 5.00)
    
    fila_compras_exemplo.adicionar_item(produto1)
    fila_compras_exemplo.adicionar_item(produto2)
    fila_compras_exemplo.adicionar_item(produto3)
    fila_compras_exemplo.adicionar_item(produto4)
    fila_compras_exemplo.listar_itens()

    print("Removendo item:", fila_compras_exemplo.remover_item())
    fila_compras_exemplo.listar_itens()

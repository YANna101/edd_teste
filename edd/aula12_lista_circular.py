from aula11_lista_ligada_ordenada import ListaLigadaOrdenada
class No:    
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class ListaLigadaCircularOrdenada:
    def __init__(self):
        self.cabeca = None

    def esta_vazia(self):
        return self.cabeca is None

    def inserir(self, dado):
        novo_no = No(dado)
        if self.esta_vazia():
            self.cabeca = novo_no
            novo_no.proximo = self.cabeca
        elif dado < self.cabeca.dado:
            atual = self.cabeca
            while atual.proximo != self.cabeca:
                atual = atual.proximo
            novo_no.proximo = self.cabeca
            atual.proximo = novo_no
            self.cabeca = novo_no
        else:
            atual = self.cabeca
            while atual.proximo != self.cabeca and dado >= atual.proximo.dado:
                atual = atual.proximo

            novo_no.proximo = atual.proximo
            atual.proximo = novo_no
            
if __name__ == "__main__":
    lista = ListaLigadaCircularOrdenada()
    lista.inserir(3)
    lista.inserir(1)
    lista.inserir(2)

    # Imprimir a lista circular ordenada
    if not lista.esta_vazia():
        atual = lista.cabeca
        while True:
            print(atual.dado, end=" -> ")
            atual = atual.proximo
            if atual == lista.cabeca:
                break
        print("(volta ao início)")
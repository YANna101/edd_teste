



from no import No

class ListaLigada:
    def __init__(self):
        self.inicio = None

    # Insere no início da lista
    def inserir_no_inicio(self, dado):
        novo_no = No(dado)
        novo_no.proximo = self.inicio
        self.inicio = novo_no

    # Remove do início da lista
    def remover_do_inicio(self):
        if self.inicio is None:
            print("A lista está vazia!")
            return None
        removido = self.inicio.dado
        self.inicio = self.inicio.proximo
        return removido

    # Exibe todos os elementos
    def exibir(self):
        atual = self.inicio
        elementos = []
        while atual is not None:
            elementos.append(str(atual.dado))
            atual = atual.proximo
        print(" -> ".join(elementos) + " -> None")

# Exemplo de uso:
if __name__ == "__main__":
    lista = ListaLigada()
    lista.inserir_no_inicio(10)
    lista.inserir_no_inicio(20)
    lista.inserir_no_inicio(30)
    lista.exibir()  # Saída: 30 -> 20 -> 10 -> None
    
    lista.remover_do_inicio()
    lista.exibir()  # Saída: 20 -> 10 -> None

    




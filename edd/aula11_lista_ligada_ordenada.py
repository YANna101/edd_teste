from no import No

class ListaLigadaOrdenada:
    def __init__(self):
        self.inicio = None

    # Insere de forma ordenada na lista
    def inserir(self, dado):
        novo_no = No(dado)
        # caso 1 e 2: a lista está vazia ou o novo dado é menor que o primeiro elemento
        if self.inicio is None or self.inicio.dado > dado: 
            novo_no.proximo = self.inicio
            self.inicio = novo_no
        else:
            # caso 3 e 4: inserir no meio ou no final da lista
            atual = self.inicio
            while atual.proximo is not None and atual.proximo.dado < dado:
                atual = atual.proximo
            novo_no.proximo = atual.proximo
            atual.proximo = novo_no

    # Remove um elemento específico da lista
    def remover(self, dado) -> None:
        if self.inicio is None:
            print("A lista está vazia!")
            return None
        
        # caso 2: o elemento a ser removido é o primeiro da lista
        if self.inicio.dado == dado:
            removido = self.inicio.dado
            self.inicio = self.inicio.proximo
            return removido
        
        # caso 3: o elemento a ser removido está no meio ou no final da lista
        atual = self.inicio
        while atual.proximo is not None and atual.proximo.dado != dado:
            atual = atual.proximo
        if atual.proximo is not None:
            removido = atual.proximo.dado
            atual.proximo = atual.proximo.proximo
            return removido
        
        print("Elemento não encontrado!")
        return None

    # Exibe todos os elementos
    def exibir(self):
        atual = self.inicio
        elementos = []
        while atual is not None:
            elementos.append(str(atual.dado))
            atual = atual.proximo
        print(" -> ".join(elementos) + " -> None")
        
    
    # Verifica se a lista está vazia
    def esta_vazia(self):
        return self.inicio is None
    
    

# Exemplo de uso:
if __name__ == "__main__":
    lista = ListaLigadaOrdenada()
    lista.inserir(10)
    lista.inserir(20)
    lista.inserir(30)
    lista.inserir(15)
    lista.exibir()  # Saída: 10 -> 15 -> 20 -> 30 -> None
    
    lista.remover(10)
    lista.exibir()  # Saída: 15 -> 20 -> 30 -> None
    
    lista.remover(20)
    lista.exibir()  # Saída: 15 -> 30 -> None
    
    print(f"A lista está vazia? {lista.esta_vazia()}")  # Saída: A lista está vazia? False


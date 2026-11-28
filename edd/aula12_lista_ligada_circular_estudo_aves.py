from no3 import no

from aula12_lista_circular import ListaLigadaCircularOrdenada


class aves:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def __str__(self):
        return f"{self.nome} ({self.especie})"


class ListaLigadaCircular:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = no(data)
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def display(self):
        if self.is_empty():
            print("A lista está vazia.")
        else:
            current = self.head
            while True:
                print(current.data, end=" -> ")
                current = current.next
                if current == self.head:
                    break
            print("(voltando ao início)")
            
            
            
    class aves:
        def __init__(self, nome, especie):
            self.nome = nome
            self.especie = especie

        def __str__(self):
            return f"{self.nome} ({self.especie})"
        
        

if __name__ == "__main__":
    lista_aves = ListaLigadaCircular()
    ave1 = aves("Papagaio", "Amazona aestiva")
    ave2 = aves("Canário", "Serinus canaria")
    ave3 = aves("Pardal", "Passer domesticus")
        
        
        
    lista_aves.append(ave1)
    lista_aves.append(ave2)
    lista_aves.append(ave3)
    
    print("Lista de aves:")
    lista_aves.display()
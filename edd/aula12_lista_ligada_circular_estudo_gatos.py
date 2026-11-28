from aula12_lista_circular import ListaLigadaCircularOrdenada
from no3 import no



class gatos:
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca

    def __str__(self):
        return f"{self.nome} ({self.raca})"
    
    
    
    
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
                
                
            
        
        
if __name__ == "__main__":
        lista_gatos = gatos.ListaLigadaCircular()
        gato1 = gatos("Mingau", "Siamês")
        gato2 = gatos("Mingal", "Persa")
        gato3 = gatos("Mingal", "Maine Coon")  
        
        lista_gatos.append(gato1)
        lista_gatos.append(gato2)
        lista_gatos.append(gato3)
        lista_gatos.display()
        
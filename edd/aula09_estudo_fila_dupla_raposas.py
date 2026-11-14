from aula09_fila_dupla import FilaDupla
class Raposa:
    def __init__(self, nome, especie, familia):
        self.nome = nome
        self.especie = especie
        self.familia = familia

    def __str__(self):
        return f"Nome: {self.nome}, Espécie: {self.especie}, Família: {self.familia}"
    
    
    
    class FilaDupla:
        def __init__(self):
            self.fila1 = []
            self.fila2 = []

        def adicionar_raposa(self, raposa):
            if len(self.fila1) <= len(self.fila2):
                self.fila1.append(raposa)
            else:
                self.fila2.append(raposa)

        def remover_raposa(self):
            if self.fila1:
                return self.fila1.pop(0)
            elif self.fila2:
                return self.fila2.pop(0)
            else:
                return None

        def mostrar_raposas(self):
            return [str(raposa) for raposa in self.fila1 + self.fila2]
    
    
    
        
if __name__ == "__main__":
    fila_raposas = FilaDupla()
    raposa1 = Raposa("Raposa Vermelha", "Vulpes vulpes", "Vulpes vulpes,familia Canidae,")
    raposa2 = Raposa("Raposa do Ártico", "Vulpes lagopus", "Vulpes lagopus,familia Canidae,")
    raposa3 = Raposa("Raposa do Deserto", "Vulpes zerda", "Vulpes zerda,familia Canidae,")
    raposa4 = Raposa("Raposa Cinzenta", "Urocyon cinereoargenteus", "Urocyon cinereoargenteus,familia Canidae,")

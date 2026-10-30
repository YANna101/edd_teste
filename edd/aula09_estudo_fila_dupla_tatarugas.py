from aula09_fila import Fila

class Tatarugas:
    def __init__(self):
        self.fila1 = Fila()
        self.fila2 = Fila()

    def adicionar_versiculo(self, especie,nome, versiculo):
        if especie == "Tartaruga1":
            self.fila1.enfileirar(versiculo)
        elif especie == "Tartaruga2":
            self.fila2.enfileirar(versiculo)

    def remover_versiculo(self):
        if not self.fila1.esta_vazia():
            return self.fila1.desenfileirar()
        if not self.fila2.esta_vazia():
            return self.fila2.desenfileirar()
        return None

    def mostrar_versiculos(self):
        return self.fila1.mostrar() + self.fila2.mostrar()
    
if __name__ == "__main__":
    tatarugas = Tatarugas()
    tatarugas.adicionar_versiculo("Tartaruga1","Leonardo", "João 3:16")
    tatarugas.adicionar_versiculo("Tartaruga2","Michelangelo", "Salmos 23:1")
    tatarugas.adicionar_versiculo("Tartaruga1","Donatello", "Filipenses 4:13")

    print("Versículos das Tartarugas:")
    print(tatarugas.mostrar_versiculos())

    versiculo_removido = tatarugas.remover_versiculo()
    print(f"Versículo removido: {versiculo_removido}")

    print("Versículos restantes das Tartarugas:")
    print(tatarugas.mostrar_versiculos())
        
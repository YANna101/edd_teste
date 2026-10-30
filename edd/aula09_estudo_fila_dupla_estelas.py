from aula09_fila import Fila

class FilaDupla(Fila):
    def __init__(self):
        super().__init__()

    def inserir_inicio(self, valor):
        self._dados.insert(0, valor)

    def remover_fim(self):
        if self.esta_vazia():
            raise Exception("Fila vazia")
        return self._dados.pop()
    
    class estelas:
        def __init__(self):
            self.fila1 = Fila()
            self.fila2 = Fila()

        def adicionar_versiculo(self, versiculo):
            self.fila1.enfileirar(versiculo)

        def remover_versiculo(self):
            if not self.fila1.esta_vazia():
                return self.fila1.desenfileirar()
            if not self.fila2.esta_vazia():
                return self.fila2.desenfileirar()
            return None

        def mostrar_versiculos(self):
            return self.fila1.mostrar() + self.fila2.mostrar()
        

if __name__ == "__main__":
    estelas = FilaDupla.estelas()
    estelas.adicionar_versiculo("Gênesis 1:1")
    estelas.adicionar_versiculo("Êxodo 20:12")
    estelas.adicionar_versiculo("Mateus 5:9")

    print("Versículos na Fila Dupla:")
    print(estelas.mostrar_versiculos())

    versiculo_removido = estelas.remover_versiculo()
    print(f"Versículo removido: {versiculo_removido}")
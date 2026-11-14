
from aula09_fila_dupla import FilaDupla

class Tatarugas:
    def __init__(self, nome, especie, nome_cientifico):
        self.nome = nome
        self.especie = especie
        self.nome_cientifico = nome_cientifico

    def __str__(self):
        return f"{self.nome} ({self.especie} - {self.nome_cientifico})"

class Tartarugas(FilaDupla):
    def __init__(self):
        self._itens = []

    def esta_vazia(self):
        return not self._itens

    def tamanho(self):
        return len(self._itens)

    def inserir_inicio(self, tartaruga):
        self._itens.insert(0, tartaruga)

    def inserir_fim(self, tartaruga):
        self._itens.append(tartaruga)

    def remover_inicio(self):
        if self.esta_vazia():
            raise IndexError("A fila dupla está vazia")
        return self._itens.pop(0)

    def remover_fim(self):
        if self.esta_vazia():
            raise IndexError("A fila dupla está vazia")
        return self._itens.pop()

    def primeiro(self):
        if self.esta_vazia():
            raise IndexError("A fila dupla está vazia")
        return self._itens[0]

    def ultimo(self):
        if self.esta_vazia():
            raise IndexError("A fila dupla está vazia")
        return self._itens[-1]

    def __len__(self):
        return self.tamanho()

    def __iter__(self):
        return iter(self._itens)


if __name__ == "__main__":
    fila_tartarugas = Tartarugas()

    tartaruga1 = Tatarugas("Tartaruga-oliva", "Tartaruga Oliva", "Lepidochelys olivacea")
    tartaruga2 = Tatarugas("Tartaruga-de-couro", "Tartaruga de Couro", "Dermochelys coriacea")
    tartaruga3 = Tatarugas("Tartaruga-cabeçuda", "Tartaruga Cabeçuda", "Caretta caretta")
    tartaruga4 = Tatarugas("Tartaruga verde", "Tartaruga Verde", "Chelonia mydas")

    fila_tartarugas.inserir_fim(tartaruga1)
    fila_tartarugas.inserir_fim(tartaruga2)
    fila_tartarugas.inserir_inicio(tartaruga3)
    fila_tartarugas.inserir_inicio(tartaruga4)

    print("Fila de Tartarugas:")
    for tartaruga in fila_tartarugas:
        print(tartaruga)

    print("\nRemovendo a primeira tartaruga:", fila_tartarugas.remover_inicio())
    print("Removendo a última tartaruga:", fila_tartarugas.remover_fim())

    print("\nFila de Tartarugas após remoções:")
    for tartaruga in fila_tartarugas:
        print(tartaruga)
                
class No:
    def __init__(self, letra, prox=None):
        self.letra = letra
        self.prox = prox


lista = [
    No('e', 1), No('h', 2), No('b', 3), No('f', 4), No('a', 5),
    No('i', 6), No('g', 7), No('c', 8), No('d', -1)
]

l = 0
while l != -1:
    print(lista[l].letra, end=' ')
    l = lista[l].prox


class Estante:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo


class Estantes:
    def __init__(self):
        self.lista = [
            Estante('romance', 1), Estante('ficção', 2), Estante('biografia', 3),
            Estante('terror', 4), Estante('a', 5), Estante('comédia', 6),
            Estante('documentário', 7), Estante('história', 8), Estante('drama', 8)
        ]

        # agora alocar a lista de livros para cada estante
        self.livros = [
            No('O Morro dos Ventos Uivantes', 1), No('1984', 2), No('Steve Jobs', 3),
            No('It: A Coisa', 4), No('O Pequeno Príncipe', 5), No('A Culpa é das Estrelas', 6),
            No('Sapiens: Uma Breve História da Humanidade', 7),
            No('A História do Mundo em 100 Objetos', 8), No('O Diário de Anne Frank', -1)
        ]


estantes = Estantes()

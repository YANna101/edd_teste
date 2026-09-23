#lista02_lista.py
#Exercício 1
# Cria uma lista sem nenhum elemento.
# A expressão lista_vazia = list() possui o mesmo efeito.
lista_vazia = []
print("Lista vazia: ", lista_vazia)
print("tipo da lista_vazia: ", type(lista_vazia))


lista_inteiros = [1, 2, 3, 4, 5]
print("Lista de inteiros: ", lista_inteiros)
print("tipo da lista_inteiros: ", type(lista_inteiros))


lista_tipos_diferentes = ["George", "Orwell", 1984]
print("Lista com tipos diferentes: ", lista_tipos_diferentes)
print("tipo da lista_tipos_diferentes: ", type(lista_tipos_diferentes))


#Exercício 2
print("Questão 02")

#lista alinada
lista_alinhada = [1, 2, 3, 4, 5]
print("Lista alinhada: ", lista_alinhada)

lista_matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Lista matriz: ", lista_matriz)


outra_lista_alinhada = [6, 7, 8, 9, 10]
print("Outra lista alinhada: ", outra_lista_alinhada)



#Exercício 3
print("Questão 03")

numeros_pares = [2, 4, 6, 8, 10]
for numero in numeros_pares:
    print("Número par: ", numero)




#Exercício 4
print("Questão 04")
#percorrendo uma lista de palavras
palavras=["cachorro", "gato", "elefante", "leão"]
for palavra in palavras:
    print("Palavra: ", palavra)
    
    
    
    #Exercício 5
print("Questão 05")
#percorrendo uma lista de palavras com índice
palavras=["cachorro", "gato", "elefante", "leão"]
for indice in range(len(palavras)):
    print("Palavra: ", palavras[indice])
    
    
    
    #Exercício 6
print("Questão 06")
#lista vazia
lista_vazia = []
#adicionando elementos na lista
lista_vazia.append("maçã")
lista_vazia.append("banana")
lista_vazia.append("laranja")
print("Lista com elementos: ", lista_vazia)


#exercício 7
print("Questão 07")
#lista de cores
lista_cores = ["vermelho", "verde", "azul"]
#adicionando elementos na lista
lista_cores.append("amarelo")
print("Lista de cores: ", lista_cores)




#exercício 8
print("Questão 08")
#lista de frutas
lista_frutas = ["maçã", "banana", "laranja"]
#adicionando elementos na lista
lista_frutas.append("uva")
print("Lista de frutas: ", lista_frutas)



#exercício 9
print("Questão 09")
#lista de cidades
lista_cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte"]
#adicionando elementos na lista
lista_cidades.append("Curitiba")
print("Lista de cidades: ", lista_cidades)




#atividade1
print("Atividade 1")

#Escreva uma função que recebe uma lista ou string x e retorna x concatenada com ela mesma.
def concatenar(x):
    return x + x

# Testando a função
print(concatenar("Hello, "))  # Saída: Hello, Hello,
print(concatenar([1, 2, 3]))  # Saída: [1, 2, 3, 1, 2, 3]




#atividade2
print("Atividade 2")

#Escreva uma função que recebe como entrada uma lista de números e retorna True se um número passado como parâmetro está presente na lista.
def esta_presente(lista, numero):
    return numero in lista

# Testando a função
print(esta_presente([1, 2, 3, 4, 5], 3))  # Saída: True
print(esta_presente([1, 2, 3, 4, 5], 6))  # Saída: False






#atividade3
print("Atividade 3")
#Escreva uma função que recebe como entrada uma lista ordenada de números e retorna o índice do primeiro elemento maior que um elementO limite. Se nenhum elemento da lista for maior que o limite desejado, retorne o valor -1.
def indice_maior_que_limite(lista, limite):
    for i in range(len(lista)):
        if lista[i] > limite:
            return i
    return -1
# Testando a função
print(indice_maior_que_limite([1, 2, 3, 4, 5], 3))  # Saída: 3
print(indice_maior_que_limite([1, 2, 3, 4, 5], 5))  # Saída: -1







#atividade4
print("Atividade 4")
#Escreva uma função que recebe como entrada uma lista de números e retorna a soma de todos os elementos da lista.
def soma_lista(lista):
    return sum(lista)

# Testando a função
print(soma_lista([1, 2, 3, 4, 5]))  # Saída: 15





#atividade5
print("Atividade 5")
#Listas em Python possuem o método reverse, que inverte o conteúdo da lista. Sua tarefa é implementar uma função chamada inverte, que possui a mesma funcionalidade básica da função reverse em Python. Por exemplo, dada a lista [1, 2, 3, 4, 5, 6, 7], sua função deve retornar [7, 6, 5, 4, 3, 2, 1].
def inverte(lista):
    return lista[::-1]

# Testando a função
print(inverte([1, 2, 3, 4, 5, 6, 7]))  # Saída: [7, 6, 5, 4, 3, 2, 1]







#atividade6
print("Atividade 6")
#Suponha que lhe seja fornecida uma lista de números. Sua tarefa é mover todos os zeros para o final da lista, preservando a ordem dos números diferentes de zero. Por exemplo, dada a lista [0, 1, 0, 3, 12], seu programa deve retornar [1, 3, 12, 0, 0].
def mover_zeros_para_final(lista):
    # Cria uma nova lista para armazenar os números diferentes de zero
    numeros_diferentes_de_zero = [num for num in lista if num != 0]
    # Conta quantos zeros existem na lista original
    quantidade_de_zeros = lista.count(0)
    # Adiciona os zeros ao final da nova lista
    numeros_diferentes_de_zero.extend([0] * quantidade_de_zeros)
    return numeros_diferentes_de_zero

# Testando a função
print(mover_zeros_para_final([0, 1, 0, 3, 12]))  # Saída: [1, 3, 12, 0, 0]







#atividade7
print("Atividade 7")
#matiz de tres por três
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#função que recebe uma matriz e retorna a soma de todos os elementos da matriz.
def soma_matriz(matriz):
    soma = 0
    for linha in matriz:
        soma += sum(linha)
    return soma

# Testando a função
print(soma_matriz(matriz))  # Saída: 45





#atividade8
print("Atividade 8")
#crie uma lista de tipos de carros, e depois crie uma função que recebe essa lista e retorna uma nova lista com os carros que começam com a letra "A".
def carros_com_a(lista_carros):
    return [carro for carro in lista_carros if carro.startswith("A")]

# Testando a função
print(carros_com_a(["Audi", "BMW", "Acura", "Ford"]))  # Saída: ["Audi", "Acura"]
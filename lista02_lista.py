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
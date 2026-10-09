# lista 3 - dicionários
# Exercício 1
print("Questão 01")
#criando um dicionário vazio
dicionario_vazio = {}
print("Dicionário vazio: ", dicionario_vazio)
paies={"Brasil": "Brasília", "Estados Unidos": "Washington, D.C.", "França": "Paris", "Japão": "Tóquio"}
print("Dicionário de países e capitais: ", paies)


# Exercício 2
print("Questão 02")
# # Modificando um dicionário.
paies["Brasil"] = "Rio de Janeiro"
print("Dicionário de países e capitais após modificação: ", paies)

# Adicionando um elemento.
espanha = {"Espanha": "Madri"}
paies.update(espanha)
print("Dicionário de países e capitais após adição: ", paies)


# Exercício 3
print("Questão 03")
# dicionário com informações de uma pessoa
pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
print("Dicionário com informações de uma pessoa: ", pessoa)


# Exercício 4
print("Questão 04")
# dicionário com informações de uma pessoa
pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
# Acessando valores do dicionário
print("Nome: ", pessoa["nome"])
print("Idade: ", pessoa["idade"])
print("Cidade: ", pessoa["cidade"])




# Exercício 5
print("Questão 05")
# dicionário com furtas

frutas = {"maçã": 2.5, "banana": 1.8, "laranja": 3.0}
# Acessando valores do dicionário
print("Preço da maçã: R$", frutas["maçã"])
print("Preço da banana: R$", frutas["banana"])
print("Preço da laranja: R$", frutas["laranja"])


# Exercício 6
print("Questão 06")
# dicionário com informações de um livro
livro = {"título": "O Senhor dos Anéis", "autor": "J.R.R. Tolkien", "ano": 1954}
# Acessando valores do dicionário
print("Título: ", livro["título"])
print("Autor: ", livro["autor"])
print("Ano: ", livro["ano"])

# Exercício 7
print("Questão 07")
# dicionário com informações de um carro
carro = {"marca": "Toyota", "modelo": "Corolla", "ano": 2020}
# Acessando valores do dicionário
print("Marca: ", carro["marca"])


# exercicio 8.1
# dicionario com uma palava
palavra="abracadabra" # ['u', 'v', 'a']
freqs = dict()
for ch in palavra:
    if ch not in freqs:
        freqs[ch] = 1
    else:
        freqs[ch] += 1

print(freqs) # {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}



# exercicio 8.2
print("questão 08")
# quando a chave não esta
palavra = "borboleta"
freqs = dict()
for ch in palavra:
    if ch not in freqs:
        freqs[ch] = 1
    else:
        freqs[ch] += 1

print(freqs) # {'b':2 , 'o':2 ,'r':1 ,'l':1 ,'e':1 ,'t':1,'a':1} 




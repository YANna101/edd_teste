# Escreva uma função que recebe dois parâmetros e imprime o menor dos dois. Se eles forem iguais, imprima que eles são iguais.
def imprimir_menor(numero1,numero2):
    if numero1<numero2:
        print(f"o numero {numero1} é o menor.")
    elif numero1>numero2:
        print(f"o numero {numero2} é o menor.")
    else:
        print(f"{numero1} e ingual ao numero {numero2}")

print("Questão 01")
imprimir_menor(3,5)
imprimir_menor(3,2)
imprimir_menor(5,5)

print("\n\n")


print("Questão 02")
#Escreva uma função que recebe um número n como parâmetro e imprime se n é positivo ou negativo
def imprimir_sinal(n):
    
    if n>=0:
        print(f"O número {n} é positivo.")
    else:
        print(f"O número {n} é negativo.")
    
imprimir_sinal(10)
imprimir_sinal(-2)


print("\n\n")
        

print("Questão 03")
#Escreva uma função para imprimir o valor absoluto de um número.
def imprimir_valor_absoluto(numero):
    if numero<0:
        print(f"o valor absoluto de {numero} é {numero*-1}")
    else:
        print(f"o valor absoluto de {numero} é {numero}")


imprimir_valor_absoluto(-5)
imprimir_valor_absoluto(5)

print("\n\n")


print("Questão 04")
#Escreva uma função que recebe dois números a e b como parâmetro e retorna True caso a soma dos dois seja maior que um terceiro parâmetro, chamado limite.
def soma_maior_que_limite(a,b,limite):
    if a+b>limite:
        return True
    else:
        return False
    
print("Verifica se 10+20>15: ", soma_maior_que_limite(10,20,15))
print("Verifica se 10+22>15: ", soma_maior_que_limite(10,2,15))

print("\n\n")



print("Questão 05")
#Escreva uma função que recebe dois números (a e b) como parâmetro e retorna a quantidade (0, 1 ou 2) deles que é maior que um terceiro parâmetro, chamado limite.
def quantidade_maior_que_limite(a, b, limite):
    quantidade = 0
    if a > limite:
        quantidade += 1
    if b > limite:
        quantidade += 1
    return quantidade

print("Valores (10, 20, 15). Maiores que o limite: ", quantidade_maior_que_limite(10, 20, 15))
print("Valores (10, 2, 15). Maiores que o limite: ", quantidade_maior_que_limite(10, 2, 15))
print("Valores (100, 20, 15). Maiores que o limite: ", quantidade_maior_que_limite(100, 20, 15))

print("\n\n")



print("Questão 06")
#Escreva uma função que recebe um número como parâmetro e para cada número menor que o parâmetro, a função imprime “Fizz” se o número for múltiplo de três, imprime “Buzz” se o número for múltiplo de cinco, e imprime “FizzBuzz” se o número for múltiplo de três e cinco. Caso o número não seja múltiplo nem de três nem de cinco, ele deve ser impresso. Note que, ao contrário das funções anteriores, sua função não deve retornar nada. Ela precisa simplesmente imprimir o que foi pedido.
def fizz_buzz(n):
    for i in range(n):
        if i % 3 == 0 and i % 5 == 0: # múltiplos de 3 e 5
            print("FizzBuzz")
        elif i % 3 == 0: # múltiplos de 3
            print("Fizz")
        elif i % 5 == 0: # múltiplos de 5
            print("Buzz")
        else: # o próprio valor
            print(i)

print("fizz_buzz(5)")
fizz_buzz(5)
print("fizz_buzz(16)")
fizz_buzz(16)
print("fizz_buzz(30)")
fizz_buzz(30)

print("\n\n")



print("Questão 07")
#Escreva uma função que, dado um número nota representando a nota de um estudante, converte o valor de nota para um conceito (A, B, C, D, E e F).
def converter_nota_para_conceito(nota):
    if nota >= 90:
        return "A"
    elif nota >= 80:
        return "B"
    elif nota >= 70:
        return "C"
    elif nota >= 60:
        return "D"
    elif nota >= 50:
        return "E"
    else:
        return "F"

print(converter_nota_para_conceito(95))
print(converter_nota_para_conceito(85))
print(converter_nota_para_conceito(75))
print(converter_nota_para_conceito(65))
print(converter_nota_para_conceito(55))
print(converter_nota_para_conceito(45))
print(converter_nota_para_conceito(35))
print(converter_nota_para_conceito(25))

print("\n\n")



print("Questão 08")
#Escreva uma função que recebe como entrada um número inteiro positivo n e retorne a soma de todos os inteiros positivos menores ou iguais a n.
def soma_inteiros_ate_n(n):
    soma = 0
    for i in range(1, n + 1):
        soma += i
    return soma

print("Soma dos inteiros menores que 5: ", soma_inteiros_ate_n(5))
print("Soma dos inteiros menores que 10: ", soma_inteiros_ate_n(10))


print("\n\n")



print("Questão 09")
#Escreva uma função que recebe como entrada um número ano e retorna True caso ano seja bissexto. Caso contrário, retorne False.
def eh_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

print("2020 é bissexto? ", eh_bissexto(2020))
print("2021 é bissexto? ", eh_bissexto(2021))



print("\n\n")



print("Questão 10")
#Escreva uma função que recebe como entrada um número n e imprime todas as potências de 2 menores ou iguais a n.
def imprimir_potencias_de_2(n):
    
    print(f"Potências de 2 menores que {n}: ")
    potencia = 1 # representa 2^0 = 1
    while potencia <= n:
        print(potencia, end="; ")
        potencia *= 2

imprimir_potencias_de_2(16)
print()
imprimir_potencias_de_2(30)



print("\n\n")



print("Questão 11")
#Escreva uma função que recebe como entrada um número inteiro positivo n e imprime a representação binária desse número.
def imprimir_representacao_binaria(n):
    if n < 0:
        print("O número deve ser positivo.")
        return
    binario = ""
    if n == 0:
        binario = "0"
    while n > 0:
        binario = str(n % 2) + binario
        n //= 2
    print(binario)

print("Representação binária de 10:")
imprimir_representacao_binaria(10)

print("Representação binária de 15:")
imprimir_representacao_binaria(15)
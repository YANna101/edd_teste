# Escreva uma função que recebe dois parâmetros e imprime o menor dos dois. Se eles forem iguais, imprima que eles são iguais.
def imprimir_menor(numero1,numero2):
    if numero1<numero2:
        print(f"o numero {numero1} é o menor.")
    elif numero1>numero2:
        print(f"o numero {numero2} é o menor.")
    else:
        print(f"{numero1} e ingual ao numero {numero2}")


imprimir_menor(3,5)
imprimir_menor(3,2)
imprimir_menor(5,5)

#Escreva uma função que recebe um número n como parâmetro e imprime se n é positivo ou negativo
def imprimir_sinal(simal1,sinal2):
    if simal1>=0:
        print(f"o sinal{simal1}é positivo")
    
    elif simal1<0:
        print(f"o sinal{simal1}é negativo")
        if sinal2>=0:
            print(f"o sinal{sinal2}é positivo")
        elif sinal2<0:
            print(f"o sinal{sinal2}é negativo")  


        

  #Escreva uma função para imprimir o valor absoluto de um número.
def imprimir_valor_absoluto(numero):
    if numero<0:
        print(f"o valor absoluto de {numero} é {numero*-1}")
    else:
        print(f"o valor absoluto de {numero} é {numero}")


        imprimir_valor_absoluto(-5)
        imprimir_valor_absoluto(5)



#Escreva uma função que recebe dois números a e b como parâmetro e retorna True caso a soma dos dois seja maior que um terceiro parâmetro, chamado limite.
def soma_maior_que_limite(a,b,limite):
    if a+b>limite:
        return True
    else:
        return False
    
print(soma_maior_que_limite(10,20,15))




#Escreva uma função que recebe dois números (a e b) como parâmetro e retorna a quantidade (0, 1 ou 2) deles que é maior que um terceiro parâmetro, chamado limite.
def quantidade_maior_que_limite(a, b, limite):
    quantidade = 0
    if a > limite:
        quantidade += 1
    if b > limite:
        quantidade += 1
    return quantidade
quantidade_maior_que_limite(10, 20, 15)



        #Escreva uma função que recebe um número como parâmetro e para cada número menor que o parâmetro, a função imprime “Fizz” se o número for múltiplo de três, imprime “Buzz” se o número for múltiplo de cinco, e imprime “FizzBuzz” se o número for múltiplo de três e cinco. Caso o número não seja múltiplo nem de três nem de cinco, ele deve ser impresso. Note que, ao contrário das funções anteriores, sua função não deve retornar nada. Ela precisa simplesmente imprimir o que foi pedido.
def fizz_buzz(n):
    for i in range(n):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
            fizz_buzz(16)
            fizz_buzz(30)





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




#Escreva uma função que recebe como entrada um número inteiro positivo n e retorne a soma de todos os inteiros positivos menores ou iguais a n.

def soma_inteiros_ate_n(n):
    soma = 0
    for i in range(1, n + 1):
        soma += i
    return soma
print(soma_inteiros_ate_n(5))
print(soma_inteiros_ate_n(10))



#Escreva uma função que recebe como entrada um número ano e retorna True caso ano seja bissexto. Caso contrário, retorne False.

def eh_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

print(eh_bissexto(2020))
print(eh_bissexto(2021))





#Escreva uma função que recebe como entrada um número n e imprime todas as potências de 2 menores ou iguais a n.

def imprimir_potencias_de_2(n):
    potencia = 1
    while potencia <= n:
        print(potencia)
        potencia *= 2

imprimir_potencias_de_2(16)
imprimir_potencias_de_2(30)




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
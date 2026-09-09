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
        elif
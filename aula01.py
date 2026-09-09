import numbers


def imprimir_maior(a, b):
    if a > b:
        print(a)
    else:
        print(b)


imprimir_maior(16, 9)
imprimir_maior(8, 8)



def imprimir_sinal(n):
    if n < 0:
        print("negativo")
    else:
        print("positivo")


imprimir_sinal(-2)
imprimir_sinal(10)



def imprimir_valor_absoluto(n):
    if n < 0:
        print(-n)
    else:
        print(n)


imprimir_valor_absoluto(-4)
imprimir_valor_absoluto(100)
imprimir_valor_absoluto(9)


for i in range(1, 17):
    imprimir_valor_absoluto(i - 8)



def imprimir_maior_de_tres(a, b, c):
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    else:
        print(c)


numeros = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)]
for a, b, c in numeros:
    imprimir_maior_de_tres(a, b, c)


class A:
    def metodo_abstrato(self):
        raise NotImplementedError("Este método deve ser implementado pelas subclasses.")

    def outro_metodo_abstrato(self):
        raise NotImplementedError("Este método deve ser implementado pelas subclasses.")


class B(A):
    def metodo_abstrato(self):
        return "implementação útil do método_abstrato"

    def outro_metodo_abstrato(self):
        return "implementação útil do outro_metodo_abstrato"


obj = B()
print(obj.metodo_abstrato())
print(obj.outro_metodo_abstrato())





#  ------------------------- Estudo laço for -------------------------


for i in range(1,6): # imprime de 1 até 5
    print(i)


for i in range(100,40,-10): # imprime essa relação 100, 90, 80, 70, 60, 50
    print(i)    


for i in range(9,40,10): # imprime essa relação 9, 19, 29, 39
    print(i)


def imprimir_indice_e_elemeto(lista):
    for i in range(5):
        print(i, " : ", lista[i])

    



def convertendo_nota_em_conceito(nota):
    if nota >= 90:
        return "A"
    elif nota >= 80:
        return "B"
    elif nota >= 70:
        return "C"
    elif nota >= 60:
        return "D"
    else:
        return "F"
    
nota=int(input("Digite a nota do aluno: "))
conceito = convertendo_nota_em_conceito(nota)
print(f"O conceito do aluno é: {conceito}")


def media(a,b):
    return (a+b)/2

media1 = media(10, 20)
print(f"A média é: {media1}")
media2 = media(15, 25)
print(f"A média é: {media2}")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media3 = media(nota1, nota2)
print(f"A média das notas digitadas é: {media3}")


# Faça um Programa que leia três números e mostre o maior e o menor deles.

numeros = []

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

numeros.append(numero1)
numeros.append(numero2)
numeros.append(numero3)

maiorNumero = sorted(numeros, reverse=True)[0]
menorNumero = sorted(numeros)[0]

print("O maior número é:", maiorNumero)
print("O menor número é:", menorNumero)
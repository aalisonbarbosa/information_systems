# Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).

while True:
    numero = int(input("Digite um número: "))

    if numero % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")
    break
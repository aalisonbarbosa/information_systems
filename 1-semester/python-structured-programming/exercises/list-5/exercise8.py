# • 8) Crie um método que receba o valor em farenheite converta a celsius

temperatura = float(input("Informe uma temperatura: "))

def converterTemperatura(temp):
    tempCel = ((temp - 32) / 1.8)

    return tempCel

print(converterTemperatura(temperatura))
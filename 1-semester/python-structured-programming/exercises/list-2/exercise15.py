# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê: 
# • salário bruto. 
# • quanto pagou ao INSS. 
# • quanto pagou ao sindicato. 
# • o salário líquido. 
# • calcule os descontos e o salário líquido, conforme a tabela à direita.

ganhoPorHora = float(input("Informe quanto ganha por hora: "))
horasTrabalhadasNoMes = float(input("Informe quantas horas trabalhou no mês: "))

salarioBruto = ganhoPorHora * horasTrabalhadasNoMes

taxaImpostoRenda = 0.11
taxaINSS = 0.08
taxaSindicato = 0.05

descontoImpostoRenda = salarioBruto * taxaImpostoRenda
descontoINSS = salarioBruto * taxaINSS
descontoSindicato = salarioBruto * taxaSindicato
totalDescontos =  descontoImpostoRenda + descontoINSS + descontoSindicato

salarioLiquido = salarioBruto - totalDescontos

print("+ Salário Bruto: R$", salarioBruto)
print("- IR (11%): R$", descontoImpostoRenda)
print("- INSS (8%): R$", descontoINSS)
print("- Sindicato (5%): R$", descontoSindicato)
print("= Salário líquido: R$", salarioLiquido)
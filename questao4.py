print("=====Questão 04=====")
valorH = float(input("Informe quanto voce ganha por horas?"))
mesH = int(input("informe as hors trabalhadas no mes ? "))

salB = valorH*mesH
impostre = salB*0.11
inss = salB*0.08
sind = salB*0.05
salL = salB - (impostre + inss + sind)

print("a. Salario bruto: R${}".format(salB))
print("b. Imposto de renda: R${}".format(impostre))
print("c. INSS: R${}".format(inss))
print("d. Sindicato: R${}".format(sind))
print("e. Salario liquido: R${}".format(salL))

input("pressione <enter> para sair")

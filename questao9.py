print("=====Questão 09======")
print("==========================================================")
print("|   FRUTAS:   |      Até 5Kg      |      Acima de 5Kg    |")
print("|  Morango    |    R$2.50 Por Kg  |      R$2.20 Por Kg   |")
print("|  Maça       |    R$1.80 Por Kg  |      R$1.50 Por Kg   |")
print("==========================================================")

compMR = int(input("Quantos Kg de morangos quer compra?\n"))
if(compMR <= 5 ):
    valorMR = compMR * 2.50
elif(compMR > 5 ):
    valorMR = compMR * 2.20
compMC = int(input("Quantos Kg de maça quer compra?\n"))
if(compMC <= 5 ):
    valorMC = compMR * 1.80
elif(compMC > 5 ):
    valorMC = compMR * 1.50

total = valorMR + valorMC

if((compMR + compMC) > 8):
    total = total - (total * 0.10)

print("Você pagará: {}".format(total))

input("pressione <enter> para sair")




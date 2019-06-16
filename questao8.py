print("=====Questão 07======")

resp = 0

p1 = input("Telefonou para a vítima?")
if(p1 == "sim"):
    resp = resp + 1
p2 = input("Esteve no local do crime?")
if(p2 == "sim"):
    resp = resp + 1
p3 = input("Mora perto da vítima?")
if(p3 == "sim"):
    resp = resp + 1
p4 = input("Devia para a vítima?")
if(p4 == "sim"):
    resp = resp + 1
p5 = input("Já trabalhou com a vítima?")
if(p5 == "sim"):
    resp = resp + 1

if(resp == 5):
    print("Classificação: Assassino")
elif(resp == 3)or(resp == 4):
    print("Classificação: Cúmprice")
elif(resp == 2):
    print("Classificação: Suspeito")
else:
    print("Classificação: Inocente")

    
input("pressione <enter> para sair")

print("=====Questão 03=====")
sexo = str(input("qual o seu sexo?[m/f]"))
h = float(input("Digite a sua altura: "))
m = (72.7*h) - 58
f = (62.1*h) - 44.7
if ( sexo == "m"):
    print("seu peso ideal é : {}".format(m))
else:
    print("seu peso ideal é : {}".format(f))
input("pressione <enter> para sair")

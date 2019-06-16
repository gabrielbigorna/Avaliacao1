print("=====Questao 11=====")

num = int(input("Digite o número que deseja ver a tabuada:\n"))
for x in range(1, 11):
    print("{} X {} = {}".format(num, x, num*x))
input("pressione <enter> para sair")

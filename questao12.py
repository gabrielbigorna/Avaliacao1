print("=====Questão 12=====")

lista = []
cont = 0 
for x in range(1, 11):
    print("Aluno {}".format(x))
    n1 = float(input("Infome sua 1° nota: "))
    n2 = float(input("Infome sua 2° nota: "))
    n3 = float(input("Infome sua 3° nota: "))
    n4 = float(input("Infome sua 4° nota: "))
    media = (n1+n2+n3+n4)/4
    lista.append(media)
    if(media >= 7):
        cont = cont + 1
print("Essa é a media dos alunos {}".format(lista))
print("Quantidade de alunos com media igual ou maior que 7: {}".format(cont))
 
input("pressione <enter> para sair")

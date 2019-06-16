print("=====Questão 07======")
sal = float(input("Informe seu salário: "))

if(sal <= 280):
    per = 20
    aut = sal * 0.20
elif(sal > 280) and(sal < 700):
    per = 15
    aut = sal * 0.15
elif(sal > 700) and (sal<1500):
    per = 10
    aut = sal* 0.10
else:
    per = 5
    aut = sal * 0.05
print("Salario antes do aumento:R${}".format(sal))
print("Percentual de aumento aplicado:{}%".format(per))
print("O valor do aumento:R${:.2f}".format(aut))
print("O novo salário:R${}".format(sal + aut))

input("pressione <enter> para sair")

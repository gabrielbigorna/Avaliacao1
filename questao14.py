print("=====Questão 14=====")

frase = input("Informe uma frase:\n")

print("a - Aparecem {} espaços em branco".format(frase.count(" ")))
print("b - Aparecem 'a'{} ".format(frase.count("a")))
print("  - Aparecem 'e'{} ".format(frase.count("e")))
print("  - Aparecem 'i'{} ".format(frase.count("i")))
print("  - Aparecem 'o'{} ".format(frase.count("o")))
print("  - Aparecem 'u'{} ".format(frase.count("u")))

input("pressione <enter> para sair")

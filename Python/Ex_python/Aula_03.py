#  Ex. Letras

def letras_or():
    letra = input("Digite uma letra:\n-> ")
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        print('A letra "' + letra +'" é uma vogal!')
    else:
        print('A letra "' + letra +'" não é uma vogal!')  

def letras_in():
    letra = input("Digite uma letra:\n-> ")
    if letra in ("a","e","i","o","u","A","E","I","O","U"):
        print('A letra "' + letra +'" é uma vogal!')
    else:
        print('A letra "' + letra +'" não é uma vogal!')


# Explicação elif

def time():
    time = input("Diga para qual time você torce: ")
    if time == "São Paulo":
        print("É o trikas não tem jeito!")
    elif time == "Palmeiras":
        print("Maior do Brasil, Tri da liberta, 12 vezes campeão brasileiro")
    elif time == "Corinthians":
        print("2005 foi roubado, parabéns pela Série B, Dívidas")
    elif time == "Santos":
        print("Parabéns pela série B, taxa baixa de natalidade")
    else:
        print("Este time não existe em nosso banco de dados!")


# Ex. elif

def imposto_salario():
    salario = float(input("Digite seu sálario(utilize ponto no lugar da vírgula): -> " ))
    if salario <= 0:
        print("Como que seu salário é negativo!")
    if salario <= 1903.99:
        print("Alíquota igual a 0%\nSeu salário será de {0}".format(salario))
    elif salario <= 2826.65:
        print("Alíquota igual a 7.5%\nSeu salário será de {0}".format(salario - (salario*(7.5/100))))
    elif salario <= 3751.05:
        print("Alíquota igual a 15%\nSeu salário será de {0}".format(salario - (salario*(15/100))))
    elif salario <= 4664.69:
        print("Alíquota igual a 22.5%\nSeu salário será de {0}".format(salario - (salario*(22.5/100))))
    else:
        print("Alíquota igual a 27.5%\nSeu salário será de {0}".format(salario - (salario*(27.5/100))))
   



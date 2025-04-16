# Ex. 01
def nota():
    nota = int(input("Digite uma nota: "))
    while not (nota >= 0 and nota <= 10):
        print("Valor Inválido!!")
        nota = int(input("Digite uma nota: "))
    print(nota)

# Ex. 02 a fazer



# Ex. 03
def pais():
    populacao_a = 80000
    populacao_b = 200000
    taxa_a = 1.03
    taxa_b = 1.015
    anos = 0

    while not (populacao_a == populacao_b):
        populacao_a = populacao_a * taxa_a
        populacao_b = populacao_b * taxa_b
        anos += 1

    print(f"A população se tornará igual em {anos} anos")

# Ex. 04
def numeros():
    soma = 0
    contador = 1
    while contador < 6:
        numero = input("Digite um número: ")
        inteiro = numero.isnumeric()
        if inteiro == True:
            soma = soma + int(numero)
            contador += 1
            media = soma/contador
            continue
        else:
            print("Este valor não é um número!")
            continue

    print(f"Soma: {soma}\nMédia: {media}")

#  Ex. 05
def intervalo():
    while True:
        n1 = input("Digite um número: ")
        n2 = input("Dgite outro número: ")
        if n1.isnumeric() == True and n2.isnumeric() == True:
            n1 = int(n1)
            n2 = int(n2)
            break
        else:
            print("Digite um valor válido!!!")
    
    if n1 > n2:
        maior = n1
        menor = n2
    else:
        maior = n2
        menor = n1

    contador = menor + 1
    while contador < maior:
        print(contador)
        contador += 1

# Ex. 06
def login():
    nome = input("Crie seu nome de usuário: ")
    senha = input("Crie uma senha: ")
    while nome == senha:
        print("Usuário e senha não podem ser iguais!!!❎👎❎")
        nome = input("Crie seu nome de usuário: ")
        senha = input("Crie uma senha: ")
    print("Dados cadastrados com sucesso!!!✅👍✅")

# Ex. 07
def tabuada():
    while True:
        numero = input("Digite um número para ver sua tabuada\n-> ")
        if numero.isnumeric() == True:
            numero = int(numero)
            multiplicador = 1
            print(f"Tabuada do {numero}")
            while multiplicador < 11:
                conta = numero * multiplicador
                print(f"{numero}X{multiplicador} = {conta}")
                multiplicador += 1
            break
        else:
            print("Digite um valor válido!!!")
            continue

# Ex. 08 a fazer
def fibonacci():
    fibonacci =  1
    print(fibonacci)
    print(fibonacci)
    contador = 1

    while contador < 90:
        contador += 1
        fibonacci = fibonacci + fibonacci

# Ex. 09 
def fatorial_f():
    while True:
        numero = input("Veja o fatorial de um número: ")
        if numero.isnumeric() == True:
            numero = int(numero)
            contador = 1
            fatorial = numero
            while contador < numero:
                fatorial = contador * fatorial
                contador += 1
            print(f"{numero}! = {fatorial}")
            break
        else:
            print("Digite um valor válido!!!")
            continue

# Ex 10
def pares_impares():
    contador = 0
    pares = 0
    while contador < 10:
        num = int(input(f"Diga o {contador+1}° número: "))
        if num%2 == 0:
            pares += 1
        contador += 1
    print(f"Você digitou:\nN° Pares: {pares}\nN° Ímpares: {10 - pares}")

# Ex. 11
def primo():
    while True:
        numero = input("Descubra se o número é primo: ")
        if numero.isnumeric():

# Ex. 12
def notas_n():
    contador = 0
    soma = 0
    while True:
        qtd = input("Digite quantas notas deseja inserir\n-> ")
        if qtd.isnumeric() == True:
            qtd = int(qtd)
            while contador < qtd:
                nota = input(f"Digite sua {contador+1}° nota\n-> ")
                if nota.isnumeric() == True and int(nota) >= 0 and int(nota) <= 10:
                    contador += 1
                    nota = int(nota)
                    soma = soma + nota
                    media = soma/contador
                else:
                    print("Digite um valor válido")
                    continue
        else:
            print("Digite um valor válido!!!")
            continue
        break
    print(f"A média final foi {media}")


    
        
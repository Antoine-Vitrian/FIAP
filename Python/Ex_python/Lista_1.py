# Lista de exercícios

# Ex. 1
def maior_numero():
    print("Compare dois números")
    n1 = input("Digite o primeiro número: ")
    n2 = input("Digite o segundo número: ")
    if n1 == n2:
        print("Os números são iguais")
    elif n1 > n2:
        print(n1, "é maior que", n2)
    else:
        print(n1, "é menor que", n2)

# Ex. 2
def votar():
    ano = int(input("Em que ano você nacseu: "))
    if ano < 2007:
        print("O seu voto é obrigatório!")
    elif ano < 2009:
        print("Você pode votar, mas não é obrigatório")
    else:
        print("Você não pode votar")

# Ex. 3
def senha():
    senha = input("Digite a senha: ")
    if senha == "1234":
        print("Acesso Permitido! Sua senha está correta!")
    else:
        print("Acesso Negado! Senha incorreta!")

# Ex. 4
def maca():
    maca = float(input("Número de maçãs que desejo comprar: "))
    if maca <= 0:
        print("Você não comprará maçãs!")
    elif maca < 12:
        preco = 0.3
    else:
        preco = 0.25
    total = maca*preco
    print(f"O preço será de R${preco:.2f}")


# Ex. 5
def numeros_cresc():
    print("Digite números diferentes")
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o primeiro número: "))
    n3 = int(input("Digite o primeiro número: "))
    if n1 < n2 and n1 < n3:
        if n2 < n3:
            print(n1, n2, n3)
        else:
            print(n1, n3, n2)
    elif n2 < n1 and n2 < n3:
        if n1 < n3:
            print(n2, n1, n3)
        else:
            print(n2, n3, n1)
    else:
        if n2 < n1:
            print(n3, n2, n1)
        else:
            print(n3, n1, n2)

def numetros_cresc_2():
    print("Digite números diferentes")
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o primeiro número: "))
    n3 = int(input("Digite o primeiro número: "))
    if n1 > n3 and n1 > n2:
        aux = n1
        n1 = n3
        n3 = aux
    elif n2 > n3:
        aux = n2
        n2 = n3
        n3 = aux
    if n2 < n1:
        aux = n1
        n1 = n2
        n2 = aux
    print(n1, n2, n3)

def numeros_cresc_3():
    print("Digite números diferentes")
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o primeiro número: "))
    c = int(input("Digite o primeiro número: "))
    maior = a
    if maior < b:
        maior = b
    if maior < c:
        maior = c

    menor = a
    if menor > b:
        menor = b
    if menor > c:
        menor = c

    meio = a + b + c - menor - maior

    print(menor,meio,maior)

def numeros_cresc_4():
    print("Digite números diferentes")
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    c = int(input("Digite o terceiro número: "))
    d = int(input("Digite o quarto número: "))

    if a > b:
        aux = a
        a = b
        b = aux
    if b > c:
        aux = b
        b = c
        c = aux
    if c > d:
        aux = c
        c = d
        d = aux
    if a > b:
        aux = a
        a = b
        b = aux
    if b > c:
        aux = b
        b = c
        c = aux
    if a > b:
        aux = a
        a = b
        b = aux
    
    print(a,b,c,d)

def numeros_cresc_5():
    print("Digite números diferentes")
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    c = int(input("Digite o terceiro número: "))

    if a > b:
        aux = a
        a = b
        b = aux
    if b > c:
        aux = b
        b = c
        c = aux
    if a > b:
        aux = a
        a = b
        b = aux
    print(a,b,c)

# Ex. 6 
def peso():
    menu = print("1. Masculino\n2. Feminino")
    sexo = int(input("Qual o seu sexo(digite o índice): "))
    if sexo != 1 and sexo != 2:
        print("Esta opção não existe!")
    altura = float(input("Qual a sua altura em metros: "))
    if sexo == 1:
        peso = (72.7*altura)-58
        print(f"Seu peso ideal é igual a {peso:.2f}")
    else:
        peso = (62.1*altura)-44.7
        print(f"Seu peso ideal é igual a {peso:.2f}")


# Ex. 7 e 8
def poligono():
    lados = int(input("Digite o n° de lados de um polígono: "))
    if lados < 3:
        print("Isto não é um polígono!")
    if lados < 5:
        print("Polígono não identificado!")
    lado = int(input("Digite o tamanho do lado\n-> "))
    perimetro = lado*lados
    if lados == 3:
        print("Perímetro igual a " +  str(perimetro) + "cm")
    elif lados == 4:
        print("Perímetro igual a " +  str(perimetro) + "cm")
    else:
        print("Perímetro igual a " +  str(perimetro) + "cm")

# Ex. 10
def triangulos():
    l1 = int(input("Diga o tamanho do primeiro lado: "))
    l2 = int(input("Diga o tamanho do segundo lado: "))
    l3 = int(input("Diga o tamanho do terceiro lado: "))
    if l1 == l2 and l2 == l3:
        print("Triângulo equilátero")
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("Triângulo isósceles")
    else:
        print("Triângulo escaleno")

# Ex. 11
def angulos():
    ang1 = int(input("Digite o primeiro ângulo: "))
    ang2 = int(input("Digite o segundo ângulo: "))
    ang3 = int(input("Digite o terceiro ângulo: "))
    soma_ang = ang1 + ang2 + ang3
    if soma_ang != 180 and (ang1 == 0 or ang2 == 0 or ang3 == 0):
        print("Isso não é um triângulo!")
    else:
        if ang1 == 90 or ang2 == 90 or ang == 90:
            print("Triângulo retângulo")
        elif ang1 > 90 or ang2 > 90 or ang > 90:
            print("Triângulo obtusângulo")
        else:
            print("Triângulo acutângulo")

# Ex. 9

# resolução 1
def maior():
    print("Digite números diferentes")
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o primeiro número: "))
    n3 = int(input("Digite o primeiro número: "))
    if n1 > n2 and n1 > n3:
        print(f"{n1} é o maior número")
    elif n2 > n3:
        print(f"{n1} é o maior número")
    else:
        print(f"{n1} é o maior número")

# resolução 2
def maior_2():
    print("Digite números diferentes")
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o primeiro número: "))
    n3 = int(input("Digite o primeiro número: "))
    if n1 < n2:
        n1 = n2
    if n2 < n3:
        n1 = n3
    print(f"{n1} é o maior número")

# resolução 3
def maior_3():
    print("Digite números diferentes")
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o primeiro número: "))
    n3 = int(input("Digite o primeiro número: "))
    maior = n1
    if b > maior:
        maior = b
    if c > maior:
        maior = c
    print(maior) 
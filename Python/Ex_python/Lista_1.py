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
        print("O preço será de R$" + str(maca*0.30))
    else:
        print("O preço será de R$" + str(maca*0.25))

# Ex. 5
def numeros_cresc():
    n1 = input("Digite o primeiro número: ")
    n2 = input("Digite o primeiro número: ")
    n3 = input("Digite o primeiro número: ")

# Ex. 6 
def peso():
    menu = print("1. Masculino\n2. Feminino")
    sexo = int(input("Qual o seu sexo(digite o índice): "))
    if sexo != 1 e sexo != 2:
        print("Esta opção não existe!")
    altura = float(input("Qual a sua altura em metros: "))
    if sexo == 1:
        peso = (72.7*altura)-58
        print(f"Seu peso ideal é igual a {peso:.2f}")
    else:
        peso = (62.1*altura)-44.7
        print(f"Seu peso ideal é igual a {peso:.2f}")

# Ex. 7
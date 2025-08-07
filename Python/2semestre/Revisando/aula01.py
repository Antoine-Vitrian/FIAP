# If e else

def macas(): 
    qtd = input("Quantas maçãs você gostaria de comprar\n-> ")
    if qtd.isnumeric == False:
        print("Valor Inválido!!!")
    else:
        qtd = int(qtd)
        preco = 0.30
        if qtd > 12:
            preco = 0.25
        preco_total = qtd * preco
        print(f"Valor da compra: R${preco_total}")

def peso_ideal():
    altura = input("Digite sua altura em cm\n-> ")
    sexo = input("Digite seu sexo(1.Feminino/2.Masculino)\n-> ")
    if altura.isnumeric() == False or sexo not in ("1","2"):
        print("Valor Inválido!!")
    else:
        altura = float(altura)
        if sexo == "1":
            peso_ideal = (62.1 * altura) - 58
        else:
            peso_ideal = (72.7 * altura) - 44.7
        print(f"Peso ideal: {peso_ideal}")

def lados():
    lados = input("Quantos lados tem o polígono\n-> ")
    if lados.isnumeric() == False:
        print("Valor Inválido!!")
    else:
        lados = int(lados)
        if lados in (2,1):
            print("Isto não é um polígono!!!")
        elif lados > 5:
            print("Polígono não encontrado em nosso banco de dados!!!")
        else:
            medida = input("Medida dos lados\n-> ")
            if medida.isnumeric() == False:
                print("Valor Inválido!!")
            else:
                medida = int(medida)
                if lados == 3:
                    print("Triângulo")
                elif lados == 4:
                    print("Quadrado")
                else:
                    print("Pentágono")
                perimetro = lados * medida
                print(f"Perímetro: {perimetro}")

def maior():
    n1 = input("Digite o 1° Número\n-> ")
    n2 = input("Digite o 2° Número\n-> ")
    n3 = input("Digite o 3° Número\n-> ")
    if n1.isnumeric() == False or n2.isnumeric() == False or n3.isnumeric() == False:
        print("Valor Inválido!!!")
    else:
        maior = n1
        if maior < n2:
            maior = n2
        if maior < n3:
            maior = n3
        print(maior)

def ordem_crescente():
    n1 = input("Digite o 1° Número\n-> ")
    n2 = input("Digite o 2° Número\n-> ")
    n3 = input("Digite o 3° Número\n-> ")
    if n1.isnumeric() == False or n2.isnumeric() == False or n3.isnumeric() == False:
        print("Valor Inválido!!!")
    else:
        if n1 > n2:
            aux = n1
            n1 = n2
            n2 = aux
        if n1 > n3:
            aux = n1
            n1 = n3
            n3 = aux
        if n2 > n3:
            aux = n2
            n2 = n3
            n3 = aux
        print(f"{n1}, {n2}, {n3}")

# while

def inf_gerais():
    nome = input("Digite seu nome\n-> ")
    while len(nome) <= 3:
        print("Nome Inválido!!!")
        nome = input("Digite seu nome\n-> ")

    idade = input("Digite sua idade\n-> ")
    while idade.isnumeric() == False or int(idade) > 150 or int(idade) < 0:
        print("Idade inválida!!!")
        idade = input("Digite sua idade\n-> ")

    salario = input("Digite seu salário\n-> ")
    while int(salario) < 0 or salario.isnumeric() == False:
        print("Salário inválido!!!")
        salario = input("Digite seu salário\n-> ")

    sexo = input("Digite seu sexo(f/m)\n-> ")
    while sexo not in ("f", "m"):
        print("Sexo inválido!!!")
        sexo = input("Digite seu sexo(f/m)\n-> ")

    est_civil = input("Estado Civil(s/c/v/d)")
    while est_civil not in ("s","c","v","d"):
        print("Opção inválida!!!")
        est_civil = input("Estado Civil(s/c/v/d)\n-> ")

def populacao():
    pop_a = 80000
    pop_b = 200000
    taxa_a = 1.03
    taxa_b = 1.015
    anos = 0
    while pop_a < pop_b:
        pop_a *= taxa_a
        pop_b *= taxa_b
        anos =+ 1
    print(f"{anos} anos")

def senha():
    usuario = input("Cadastre seu usuário\n-> ")
    senha = input("Cadastre sua senha\n-> ")
    while usuario == senha:
        print("Erro!!! Usuário e Senha iguais")
        usuario = input("Cadastre seu usuário\n-> ")
        senha = input("Cadastre sua senha\n-> ")
    print("Usuário cadastrado com sucesso")

def tabuada():
    numero = input("Gostaria de ver a tabuada de qual número\n-> ")
    while numero.isnumeric() == False:
        print("Valor Inválido!!!")
        numero = input("Gostaria de ver a tabuada de qual número\n-> ")
    numero = int(numero)
    multiplicador = 0
    while multiplicador <= 10:
        print(f"{numero}x{multiplicador} = {numero*multiplicador}")
        multiplicador += 1
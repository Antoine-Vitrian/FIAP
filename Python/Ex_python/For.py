def exp1():
    vogais = 0
    for char in 'danilo':
        if char in ['a','e','i','o','u']:
            vogais += 1
    print(vogais)

def range1():
    for i in range(1, 10, 3):
    # começa no 1 acaba no 10
    # de 3 em 3
        print(i)

def tabuada_for():
    for i in range(1, 11):
        print(f"\nTabuada do {i}:")
        for j in range(1, 11):
            print(f"{i}x{j} = {i*j}")

def lista_for1():
    lista = [3, True, 1.5, "danilo", []]
    for elem in lista:
        print(elem)

def prof():
    profs = ['Danilo', 'André', 'Celso']
    materias = ['Python', 'Historinha', 'Matemática']
    for i in range(len(profs)):
            print(f"{profs[i]} dá {materias[i]}")

def alunos():
    alunos = ['Lucas Sena', 'Rhariel', 'Sara', 'Isabela', 'Lucas Zago']
    notas = [8, 8.5, 6, 4, 1]
    for i in range(len(alunos)):
        if notas[i] >= 6:
            print(f'{alunos[i]}: Aprovado')
        else:
            print(f"{alunos[i]}: Reprovado")

def numeros():
    numeros = [4, 9, 2, 5, 7, 1, 0, 8, 3, 6]
    pares = 0
    soma = 0
    for i in range(len(numeros)):
        if numeros[i] % 2 == 0:
            pares += 1
        soma += numeros[i]
    media = soma/len(numeros)
    print(f"Pares: {pares}\nSoma: {soma}\nMédia: {media}")

def lista_num():
    numeros = []
    for i in range(10):
        num = input("Digite um número\n-> ")
        while not num.isnumeric():
            print("Valor Inválido!!!")
            num = input("Digite um número\n-> ")
        num = int(num)
        numeros.append(num)
    print(numeros)

def maior():
    lista = [1, 5, 6, 2, 3, 9, 10, 7, 8, 4]
    maior = lista[0]
    for i in range(len(lista)):
        print(f"Vou testar se {lista[i]} > {maior}")
        if lista[i] > maior:
            print(f"Deu certo, vou trocar {maior} por {lista[i]}")
            maior = lista[i]
            indice_maior = i
    print(f"Maior Número em {lista} é {maior}")
    print(f"Indice igual a {indice_maior}")

maior()
    
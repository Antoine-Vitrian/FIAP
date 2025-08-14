def tabuada_while():
    i = 1
    while i < 11:
        print(f"Tabuada do {i}:")
        j = 1
        while j < 11:
            print(f"{i}x{j} = {i*j}")
            j += 1
        i += 1
        print("")

def tabuada_for():
    for i in range(1,11):
        print(f"Tabuada do {i}:")
        for j in range(1,11):
            print(f"{i}x{j} = {i*j}")
        print("")

# Listas

def test01_lista():
    lista = [3, "danilo", 0.5, True]
    for i in range(len(lista)):
        print((f"lista[{i}] = {lista[i]}"))

    for elem in lista:
        print(elem)


# Ex 01
def soma_media():
    lista = [12, 56, 4, 99, 17, 70]
    soma = 0
    media = 0

    for i in range(len(lista)):
        soma += lista[i]
        media = soma/(i+1)
    print(f"Soma = {soma}\nMédia = {media}")

# Ex 02
def lista_num():
    lista = []

    def verifica_numero(msg):
        num = input(msg)
        while not num.isnumeric():
            num = input(msg)
        num = int(num)
        return num

    qtd = verifica_numero("Quantos Números você gostaria de ter na lista?\n-> ")
    for i in range(qtd):
        num = verifica_numero("Diga um número:\n-> ")
        lista.append(num)

    pares = 0
    for i in range(len(lista)):
        if lista[i]%2==0:
            pares += 1
    print(f"Pares: {pares}\nÍmpares: {len(lista) - pares}")

# Função média
def calcular_media(lista):
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]
    media = soma/len(lista)
    return media

# Função maior valor
def maior_valor(lista):
    indice_maior = 0
    maior = lista[indice_maior]
    for i in range(len(lista)):
        if maior < lista[i]:
            indice_maior = i
            maior = lista[indice_maior]
    return maior

lista01 = [2, 3, 65, 145, 987]
# maior01 = maior_valor(lista01)
# print(maior01)

lista = []
vogal = input("Digite uma vogal\n-> ")
while True:
    if vogal not in ("a", "e", "i", "o", "u"):
        vogal = input("Digite uma vogal\n-> ")
        continue
    else:
        lista.append(vogal)
        break
print(lista)
    
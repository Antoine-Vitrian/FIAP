
# def forca_opcao(msg, lista_opcoes):
#     opcoes = "\n".join(lista_opcoes)
#     print(opcoes)
#     escolha = input(msg)
#     while not escolha in lista_opcoes:
#         escolha = input(msg)
#     return escolha

# while True:
#     vinhos =  ["Pergola", "Sague de Boi", "Salton"]
#     vinho = forca_opcao("Qual vinho você quer", vinhos)
#     print(f"Você escolheu o {vinho}")
#     opcoes = ["s", "n"]
#     continuar = forca_opcao("Você quer continuar? (s/n)", opcoes)
#     if continuar == "s":
#         continue
#     else:
#         break


# def media_num(lista_num):
#     soma = 0
#     for i in lista_num:
#         soma += i
#     media = soma/len(lista_num)
#     return media

# numeros = [1, 3, 4, 6, 5]
# acha_media = media_num(numeros)
# print(acha_media)

# numeros1 = [1, 3, 1, 9, 1]
# acha_media = media_num(numeros1)
# print(acha_media)


# DEF pares
# def ver_pares(lista_num):
#     pares = 0
#     for num in lista_num:
#         if num%2 == 0:
#             pares+=1
#     return pares

# lista1 = [1, 2, 2, 6, 1, 9]
# print(ver_pares(lista1))




def maior_num(lista_maior):
    maior = lista_maior[0]
    indice_maior = 0
    for i in range(len(lista_maior)):
        if lista_maior[i] > maior:
            maior = lista_maior[i]
            indice_maior = i
    return f"Indice: {indice_maior}\nValor: {maior}"

# lista1 = [9, 2, 12, 3, 1]
# print(maior_num(lista1))
# print("")
# lista2 = [2, 1, 9, 19]
# print(maior_num(lista2))


def forca_opcao(msg, lista_opcoes):
    opcoes = "\n".join(lista_opcoes)
    print(opcoes)
    escolha = input(msg)
    while not escolha in lista_opcoes:
        escolha = input(msg)
    return escolha

def acha_index(lista, elem):
    for i in range(len(lista)):
        if lista[i] == elem:
            return i

def join_py(lista, esp):
    ajuntado = lista[0]
    for i in range(1,len(lista)):
        ajuntado += esp + lista[i]
    return ajuntado

lista_test = ["Palmeiras", "Tottenham", "Fenerbahce"]
print(join_py(lista_test," -espaço- "))


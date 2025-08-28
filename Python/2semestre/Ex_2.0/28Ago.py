import random
from random import randint
from matplotlib import pyplot as plt

matriz01 = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
# print(matriz01[0])
# print(type(matriz01[0]))
# print(matriz01[0][2])

def elementos_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(f"matriz[{i}][{j}] = {matriz[i][j]}")
    return

def mostra_matriz(matriz):
    for linha in matriz:
        print(linha)
    return

def criar_matrizes(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            coluna = random.randint(1, 100)
            linha.append(coluna)
        matriz.append(linha)
    return matriz
    
def grafico_matriz(matriz):
    plt.imshow(matriz)
    plt.colorbar()
    plt.show()

def diagonal_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == j:
                matriz[i][j] = 1
    return matriz

def digonal_bom(matriz):
    for i in range(len(matriz)):
        matriz[i][i] = 1
    return matriz

def contra_diagonal(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i + j == (len(matriz) - 1):
                matriz[i][j] = 1
    return matriz

def contra_diagonal_bom(matriz):
    for i in range(len(matriz)):
        j = len(matriz) - i - 1
        matriz[i][j] = 1
    return matriz

def matriz_x(matriz):
    for i in range(len(matriz)):
        j = len(matriz) - i - 1
        matriz[i][j] = 1
        matriz[i][i] = 1
    return matriz

def xadrez_matriz(xadrez):
    for i in range(len(xadrez)):
        for j in range(len(xadrez)):
            if i%2 == 0:
                if j%2 == 0:
                    xadrez[i][j] = 0
                else:
                    xadrez[i][j] = 1
            else:
                if j%2 == 0:
                    xadrez[i][j] = 1
                else:
                    xadrez[i][j] = 0
    return xadrez

def xadrez_bom(xadrez):
    for i in range(len(xadrez)):
        for j in range(len(xadrez)):
            if i%2 == j%2:
                xadrez[i][j]
            else:
                xadrez[i][j]
    return xadrez

def jMaiorI(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j>i:
                matriz[i][j] = 1
    return matriz

def jMenorI(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j<i:
                matriz[i][j] = 1
    return matriz

def transpor_matriz(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    transposta = []
    for j in range(colunas):
        nova_linha = []
        for i in range(linhas):
            nova_linha.append(matriz[i][j])
        transposta.append(nova_linha)
    return transposta

def transposta_boa(matriz):
    for i in range(len(matriz)):
        for j in range(i):
            aux = matriz[i][j]
            matriz[i][j] = matriz[j][i]
            matriz[j][i] = aux
    return matriz


matriz01 = criar_matrizes(2,3)
mostra_matriz(matriz01)
print()
matriz01 = transpor_matriz(matriz01)
mostra_matriz(matriz01)





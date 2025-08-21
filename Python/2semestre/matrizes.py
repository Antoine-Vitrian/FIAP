from matplotlib import pyplot as plt
import random

# matriz = [[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]]

# print(matriz[0])
# print(matriz[0][2])

# for i in range(len(matriz)):
#     for j in range(len(matriz[i])):
#         print(f"{matriz[i][j]}")

def criar_matrizes(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            # coluna = random.randint(1, 100)
            linha.append(0)
        matriz.append(linha)
    return matriz

def mostra_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])
    return
        
diagonal = criar_matrizes(100, 100)
for i in range(len(diagonal)):
    diagonal[i][i] = 1

xadrez = criar_matrizes(8, 8)
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

circulo = criar_matrizes(1000, 1000)
raio = len(circulo)/2
for i in range(len(circulo)):
    for j in range(len(circulo[0])):
        if (i-raio)**2 + (j-raio)**2 <= raio**2:
            circulo[i][j] = i
        else:
            circulo[i][j] = 0


mostra_matriz(circulo)
plt.imshow(circulo,cmap="hot")
plt.colorbar()
plt.show()

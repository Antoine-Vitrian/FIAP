import time
import sys

# a) Countdown (linha nova)
print("a) Countdown (linha nova):")
# Loop para contagem
for i in range(5, 0, -1):
    # Print do número
    print(i)
    # O código tem uma pausa de um segundo para prosseguir
    time.sleep(1)
print("Tempo esgotado!\n")

# b) Countdown (substituindo a linha)
print("b) Countdown (substituindo a linha):")
# Loop para contagem
for i in range(5, 0, -1):
    # Print do número
    print(f"\r{i}", end="")
    # Faz o próximo número aparecer na mesma linha imediatamente
    sys.stdout.flush()
    # O código tem uma pausa de um segundo para prosseguir
    time.sleep(1)
print("\rTempo esgotado!\n")

# c) Status de carregamento
print("c) Status de carregamento:")
for i in range(21):
    barra = "#" * i + "-" * (20 - i)
    print(f"\rCarregando: [{barra}] {i * 5}%", end="")
    sys.stdout.flush()
    time.sleep(0.2)
print("\nConcluído!")


import random
import string

# Gera uma senha aleatória
def gerar_senha(tamanho=12):
    # Conjunto de caracteres possíveis
    caracteres = string.ascii_letters + string.digits + string.punctuation

    # Gera a senha escolhendo caracteres aleatórios
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha


# Exemplo de uso
tamanho = int(input("Digite o tamanho da senha: "))
senha = gerar_senha(tamanho)
print("Senha gerada:", senha)


import math

# a) Função para calcular o comprimento do círculo
def comprimento_circulo(raio):
    return 2 * math.pi * raio

# b) Função para calcular o número de voltas
def numero_de_voltas(raio, distancia):
    comprimento = comprimento_circulo(raio)
    voltas = distancia / comprimento
    return voltas

# Exemplo de uso
raio = float(input("Digite o raio da pista (em metros): "))
distancia = float(input("Digite a distância percorrida (em metros): "))

voltas = numero_de_voltas(raio, distancia)

print(f"O atleta deu aproximadamente {voltas:.2f} voltas na pista.")

import math


# Função para calcular o discriminante (∆)
def discriminante(a=0, b=0, c=0):
    return b ** 2 - 4 * a * c


# Função para verificar se o discriminante é positivo
def delta_positivo(a=0, b=0, c=0):
    delta = discriminante(a, b, c)
    return delta > 0


# Função para calcular as raízes reais de uma equação do 2º grau
def raizes_reais(a=0, b=0, c=0):
    if a == 0:
        return "Não é uma equação do segundo grau (a deve ser diferente de 0)."

    delta = discriminante(a, b, c)

    if not delta_positivo(a, b, c):
        return "O discriminante não é positivo. Não há raízes reais."

    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)

    return x1, x2


# Exemplo de uso
a = 1
b = -5
c = 6

print(f"Discriminante: {discriminante(a, b, c)}")

if delta_positivo(a, b, c):
    print(f"As raízes reais são: {raizes_reais(a, b, c)}")
else:
    print("Não há raízes reais.")

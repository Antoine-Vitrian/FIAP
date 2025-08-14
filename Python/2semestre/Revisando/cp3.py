# Verifica Número
def verifica_numero(msg, erro):
        num = input(msg)
        while not num.isnumeric():
            print(erro)
            num = input(msg)
        num = int(num)
        return num

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

# Função menor valor
def menor_valor(lista):
    indice_menor = 0
    menor = lista[indice_menor]
    for i in range(len(lista)):
        if menor > lista[i]:
            indice_menor = i
            menor = lista[indice_menor]
    return menor



# SISTEMA
print("Boas Vindas!!!")
ano_nascimento = verifica_numero("Ano de Nascimento\n-> ", "Erro!!!")

ano_nascimento = int(ano_nascimento)
if (2025 - ano_nascimento) < 18:
    print("Acesso negado")
    endereco = ("Endereço\n-> ")
else:
    listaOpcoes = ["Vinho1", "Vinho2", "Vinho3"]
    precos = [120, 250, 310]
    precoMedio = calcular_media(precos)
    maiorPreco = maior_valor(precos)
    menorPreco = menor_valor(precos)
    print(f"""
    Preço Médio: {precos[precoMedio]}
    Maior Preço: {precos[maiorPreco]}
    Menor Preço: {precos[menorPreco]}
""")
    
    

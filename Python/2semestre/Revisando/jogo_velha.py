# Função de conferência jogada
def conferir_jogada(indice, msg, jogador, jogadas_validas):
    print(jogador)
    jogada = input(msg)
    while indice not in (jogadas_validas):
        jogada = input(msg)
        return jogada

lista_tabuleiro = [1, 2, 3, 4, 5, 6, 7, 8, 9]
tabuleiro = print(f"""
    -------------
    | {lista_tabuleiro[0]} | {lista_tabuleiro[1]} | {lista_tabuleiro[2]} |
    -------------
    | {lista_tabuleiro[3]} | {lista_tabuleiro[4]} | {lista_tabuleiro[5]} |
    -------------
    | {lista_tabuleiro[6]} | {lista_tabuleiro[7]} | {lista_tabuleiro[8]} |
    -------------
""")


# Jogo da velha no terminal
print("Bem vindo ao jogo da velha multiplayer!!!")

# Menu de opções
print(
    '''
Escolha sua peça:
    1- O
    2- X
''')

# Conferindo se a escolha é válida
peca = input("Escolha suas peças:\n-> ")
while peca not in ("1", "2"):
    print("Escolha inválida!!!")
    peca = input("Escolha suas peças:\n-> ")

# Explicando as regras
print('''
Na sua vez você precisa digitar o índice do local do tabuleiro conforme a tabela abaixo
      
    -------------
    | 1 | 2 | 3 |
    -------------
    | 4 | 5 | 6 |
    -------------
    | 7 | 8 | 9 |
    -------------
''')
jogadas = 0
while True:
    jogada1 = conferir_jogada()



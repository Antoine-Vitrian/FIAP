# Importação de bibliotecas necessáriasclear
import random

# Lista de times
times_de_futebol = [
    "Flamengo",
    "Palmeiras",
    "Corinthians",
    "São Paulo",
    "Santos",
    "Grêmio",
    "Internacional",
    "Atlético Mineiro",
    "Cruzeiro",
    "Botafogo",
    "Vasco da Gama",
    "Fortaleza",
    "Bahia",
    "Ceará",
    "Athletico Paranaense",
    "Barcelona",
    "Real Madrid",
    "Manchester United",
    "Liverpool",
    "Bayern de Munique",
    "Paris Saint-Germain",
    "Juventus",
    "Milan",
    "Inter de Milão",
    "Ajax"
]

# Times Sorteados
times_sort = []
# Times Escolhidos Salvos
times_esc_salvos = []

def campeonato_mata_mata():
    # Mostra os times dispóníveis
    for i in range(len(times_de_futebol)):
        print(f"{times_de_futebol[i]}")
    times_esc = 0
    print("")
    # Escolha dos Times
    while times_esc < 2:
        escolha = input(f"{times_esc + 1}° Time: ")
        # Verifica se o time é válido
        if escolha not in(times_de_futebol):
            print("Time Inválido!!!")
        else:
            # Adiciona o time a uma lista de times escolhidos salvos
            times_esc_salvos.append(escolha)
            times_esc += 1
    # Sorteio dos times para fazer o chaveamento
    for time in range(len(times_esc_salvos)):
        esc_ale = times_esc_salvos.pop(random.randrange(len(times_esc_salvos)))
        times_sort.append(esc_ale)
    
    

    

        

    
   
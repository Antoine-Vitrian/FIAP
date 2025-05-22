# Importação de bibliotecas necessárias
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
    while times_esc < 8:
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

    espaco = ""
    # Sorteio com chaveamento no print
    print(f'''
            Quartas
 ---------------------------- 
 | {times_sort[0].ljust(20)} |   |
 -------------------------------------
 | {times_sort[1].ljust(20)} |   |        |         ----------------------------
 ----------------------------        |         | {espaco.ljust(20)} |   |
                                     ------------------------------------------------
 ----------------------------        |         | {espaco.ljust(20)} |   |         |
 | {times_sort[2].ljust(20)} |   |        |         ----------------------------         |
 -------------------------------------                                              |
 | {times_sort[3].ljust(20)} |   |                                                       |         -----------------------------
 ----------------------------                                                       |         | {espaco.ljust(20)} |    |
                                                                                    --------------------------------------
 ----------------------------                                                       |         | {espaco.ljust(20)} |    |
 | {times_sort[4].ljust(20)} |   |                                                       |         -----------------------------
 -------------------------------------                                              |
 | {times_sort[5].ljust(20)} |   |        |         ----------------------------         |
 ----------------------------        |         | {espaco.ljust(20)} |   |         |
                                     ------------------------------------------------
 ----------------------------        |         | {espaco.ljust(20)} |   |         
 | {times_sort[6].ljust(20)} |   |        |         ----------------------------                                               
 -------------------------------------                                                   
 | {times_sort[7].ljust(20)} |   |                                                            
 ----------------------------
''')

    # Avanço para próxima fase
    print("Sorteie os resultados da próxima fase")
    input("Pressione qualquer tecla para avançar")

    # Sorteio Resultados
    result_quartas = []
    for i in range(8):
        result_quartas.append(random.randint(1, 5))

    # Conferindo Pênaltis
    penaltis = []
    semi = []
    for i in range(0, len(result_quartas), 2):
        if result_quartas[i] == result_quartas[i+1]:
            print("Penaltis")
        else:
            penaltis.append("")
            semi.append




# campeonato_mata_mata()

    

    

        

    
   
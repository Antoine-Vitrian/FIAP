# Importação da Biblioteca Random
import random
import listas
# Lista de Times
times_brasileirao_2025 = [
    {
      "time": "Atlético-MG",
      "pontos": 0,
      "jogos": 38,
      "vitorias": 0,
      "empates": 0,
      "derrotas": 0,
      "gp": 0,
      "gc": 0,
      "sg": 0
    },
    "Bahia",
    "Botafogo",
    "Ceará",
    "Corinthians",
    "Cruzeiro",
    "Flamengo",
    "Fluminense",
    "Fortaleza",
    "Juventude",
    "Grêmio",
    "Internacional",
    "Mirassol",
    "Palmeiras",
    "RB Bragantino",
    "Santos",
    "São Paulo",
    "Sport",
    "Vasco",
    "Vitória"
]

lista_gols = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    2, 2, 2, 2, 2, 2, 2, 2,
    3, 3, 3, 3, 3,
    4, 4, 4,
    5,
    6,
    7
]

def campeonato():
    for i in len(times_brasileirao_2025):
        print("Jogos em Casa {}")
        for j in len(times_braisleirao_2025):


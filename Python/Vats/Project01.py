def granPrix_calendar():
    n_granPrix = input("Quantos Gran Prix terá o calendário?\n-> ")
    while n_granPrix.isnumeric() == False:
        print("Digite um valor válido!!!")
        n_granPrix = input("Quantos Gran Prix terá o calendário?\n-> ")
    granPrix = []
    contador = 0
    while contador < int(n_granPrix):
        nome_gp = input(f"Digite o nome do {contador+1}° Gran Prix\n-> ")
        granPrix.append(nome_gp)
        contador += 1
    print(granPrix)

granPrix_calendar()
    

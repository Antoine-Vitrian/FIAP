def contador_char():
    n_char = 0
    text = input("Digite seu texto\n-> ")
    for i in text:
        n_char +=1
    print(f"Carcteres: {n_char}")

def gp():
    pilotos = ["Alex Albon", "Lewis Hamilton", "Max Verstappen", "Oscar Piastri"]
    gran_prix = ["", "", ""]

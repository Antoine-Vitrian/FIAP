# Ex. 01

nota = int(input("Digite uma nota: "))
while not (nota >= 0 and nota <= 10):
    print("Valor Inválido!!")
    nota = int(input("Digite uma nota: "))
print(nota)
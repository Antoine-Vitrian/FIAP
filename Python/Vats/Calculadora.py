import math

def calculadora():
    entrar = input("Gostaria de entrar na calculadora(s/n): ")
    contador = 0
    if entrar == "s" or entrar == "S":
        usuario = input("Digite seu nome de usuário: ")
        while True:
            menu = print('''
            1. Adição
            2. Subtração
            3. Multiplicação
            4. Divisão
            5. Potenciação
            6. Raiz quadrada
            7. Equação de 2° grau
            8. Sair''')
            print(menu)
            operacao = input("Escolha uma operação(digite o índice): ")
            if operacao not in ("1", "2", "3", "4", "5", "6", "7", "8"):
                print("Esta opção não existe!")
                continue
            if operacao == "8":
                sair = input("Você realmente gostaria de sair da calculadora(s/n): ")
                if sair == "s" or sair == "S":
                    break
                if sair == "n" or sair == "N":
                    continue
            contador += 1
            if operacao == "7":
                print("Ex. de equação: ax² +/- bx +/- c")
                print("Lembre de usar (+/-) para definir se o número é positivo ou negativo")
                a = int(input("Digite a:\n-> "))
                b = int(input("Digite b:\n-> "))
                c = int(input("Digite c:\n-> "))

                delta = (b**2)-(4*a*c)
                if delta < 0:
                    print("ERRO!\nEssa calculadora não faz operações com números complexos!")
                else:
                    x1 = (-b + (delta**(1/2)))/(2*a)
                    x2 = (-b - (delta**(1/2)))/(2*a)

                    print(f"A equação {a}x²{b}x{c}=0 tem como resultados:\nx1 = {x1}\nx2 = {x2}")
                    continue
            if operacao == "6":
                raiz = int(input("Digite um número: "))
                raiz_calculada = math.sqrt(raiz)
                print(round(raiz_calculada, 2))
                continue
            n1 = int(input("Digite o primeiro número: "))
            n2 = int(input("Digite o segundo número: "))
            if operacao == "1":
                print(f"{n1} mais {n2} igual a {n1+n2}")
                continue
            if operacao == "2":
                print(f"{n1} menos {n2} igual a {n1-n2}")
                continue
            if operacao == "3":
                print(f"{n1} multiplicado por {n2} igual a {n1*n2}")
                continue
            if operacao == "4":
                print(f"{n1} dividido por {n2} igual a {round(n1/n2, 2)}")
                continue
            if operacao == "5":
                print(f"{n1} elevado a {n2} igual a {n1**n2}")
                continue
        relatorio = input("Gostaria de imprimir relatório(s/n): ")
        if relatorio not in ("s", "n"):
            print("Erro 404")
        elif relatorio == "s":
            print(f"{usuario}\nContas realizadas: {contador}")

        print("Obrigado por usar a calculadora, volte sempre!")

    else:
        print("Que pena! Você não quis usar nossa calculadora!")


# Chamando a função calculadora
calculadora()

# login para a calculadora
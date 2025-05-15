ano = input("Diga seu ano de nascimento: ")
while not ano.isnumeric():
    ano = input("Diga seu ano de nascimento: ")
    ano = int(ano)
    vinho1 = "Pérgola"
    vinho2 = "Sangue de boi"
    vinho3 = "Cantinho do vale"
    preco1 = 10
    preco2 = 20
    preco3 = 30
    qtd1 = 0
    qtd2 = 0
    qtd3= 0
    valor_total = 0

    idade = 2025 - ano
    if idade < 18:
        print("Que feio, vou contar para sua mãe!")
    else:
        endereco = input("Diga seu endereço: ")
        while True:
            escolha = input(f"Essas são nossas opções:\n{vinho1} - {preco1}\n"
                            f"{vinho2} - {preco2}\n{vinho3} - {preco3}\n"
                            f"Qual você quer?\n-> ")
            while not (escolha == vinho1 or escolha == vinho2 or escolha == vinho3):
                escolha = input(f"Essas são nossas opções:\n{vinho1} - {preco1}\n"
                            f"{vinho2} - {preco2}\n{vinho3} - {preco3}\n"
                            f"Qual você quer?\n-> ")
            
            qtd = input(f"Quantas garrafas de {escolha} você quer\n-> ")
            while not qtd.isnumeric():
                print("Inválido")
                qtd = input(f"Quantas garrafas de {escolha} você quer\n-> ")
            qtd = int(qtd)

            if escolha == vinho1:
                preco = preco1
                qtd1 += qtd
            elif escolha == vinho2:
                preco = preco2
                qtd2 += qtd
            else:
                preco = preco3
                qtd3 += qtd
            valor_total += qtd*preco
            continuar = input("Você quer continuar comprando(s/n)\n-> ")
            while not (continuar == "s" or continuar == "n"):
                continuar = input("Você quer continuar comprando(s/n)\n-> ")
            if continuar == 'n':
                break
        frete = 10
        if valor_total >= 500:
            print("Frete Grátis")
            frete = 0
        valor_total += frete
        print(f"Obrigado por comprar aqui!Você comprou:\n{qtd1} - {vinho1}\n"
              f"{qtd2} - {vinho2}\n{qtd3} - {vinho3}\nTotalizando em R${valor_total} "
              f"e seu pedido será entregue em {endereco}")
            




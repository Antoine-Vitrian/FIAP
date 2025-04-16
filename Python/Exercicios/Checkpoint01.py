print("Seja bem vindo/a à vinheria Agnello!!!")
ano = int("Diga seu ano de nascimento: ")
idade = 2025 - ano
if idade < 18:
    print("QUE FEIO!!! VO CONTA P SUA MÃE!!!")
else:
    vinho1 = "Pérgola"
    vinho2 = "Sangue de Boi"
    vinho3 = "Cantinho do vale"
    preco1 = 50
    preco2 = 30
    preco3 = 10
    escolha = input(f"Esses são nossos vinhos:\n{vinho1} - {preco1}"
                    f"\n{vinho2} - {preco2}\n{vinho3} - {preco3}"
                    f"Qual você quer?\n-> ")
    
    qtd = int(input(f"Quantas garrafas de {escolha} você quer?\n-> "))
    if escolha == vinho1:
        preco = preco1
    elif escolha == vinho2:
        preco = preco2
    else:
        preco = preco3
    total = qtd*preco
    if total < 100:
        frete = 10
        total = total + frete
    else:
        print("Frete grátis!!!")
    print(f"Sua compra ficou {total}")

    
    

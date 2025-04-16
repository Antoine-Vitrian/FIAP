def pares():
    i = 0
    pares = 0
    qtd = int(input("Quantos números você quer digitar:\n ->"))
    while i < qtd:
        num = int(input(f"Diga o {i+1}° número: "))
        if num%2 == 0:
            pares = pares + 1 
        i += 1
    print(f"Você digitou:\nN° Pares: {pares}\nN° Ímpares: {i - pares}")


# Ex. 01 

def senha():
    i = 0
    senha = "1234"
    while i < 3:
        tentativa = input("Digite a senha: ")
        if tentativa == senha:
            print("Acesso liberado!")
            break
        else:
            print("Senha Incorreta!!!")
            i += 1
    if i == 3:
        print("Acesso Bloqueado!!!")
        
# Controle de Senha
def login():
    from logins_senhas import *
    i = 0

    print('''
    1. Login
    2. Cadastre-se
    ''')
    options_login = input("Digite o índice para entrar\n-> ")
    if options_login == "1":
        while i < 3:
            t_usuario = input("Usuário: ")
            t_senha = input("Senha: ")
        if t_senha == senhas and t_login = logins:
            print("Acesso liberado!")
            break
        else:
            print("Senha Incorreta!!!")
            i = i + 1
    if i == 3:
        print("Acesso Bloqueado!!!")
            

# ex 02

def genero():
    sexo = input("Digite seu sexo: ")
    while sexo != "masculino" and sexo != "feminino":
        print("Digite um sexo válido!")
        sexo = input("Digite seu sexo: ")
    print("Prossiga.")


def numero():
    numero = input("Digite algo: ")
    conf_n = numero.isnumeric()
    while conf_n == False :
        print("Valor inválido!")
        numero = input("Digite algo: ")
        conf_n = numero.isnumeric()
    print("Finish the code!")



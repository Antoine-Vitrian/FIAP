import pandas as pd
import requests

# defs
def forca_opcao(msg,lista_opcoes):
    msg += '\n- '.join(lista_opcoes) + '\n-> '
    opcao = input(msg)
    while opcao not in lista_opcoes:
        print("Erro!")
        opcao = input(msg)
    return(opcao)

def acha_indice(lista,elem):
    for i in range(len(lista)):
        if lista[i] == elem:
            return i
        
def cria_indice(lista):
    indices = {}
    for i in range(len(lista)):
        indices[lista[i]] = i
    return indices

def create(lista):
    for key in lista.keys():
        info = input(f"Diga o novo {key}: ")
        lista[key].append(info)
    return

def delete(lista):
    escolha = forca_opcao("Lista de carnes\n",acougue['Carnes'])
    indice_esc = indices[escolha]
    for key in lista.keys():
        lista[key].pop(indice_esc)
    return

def read(lista,indice):
    for i in lista.keys():
        print(f"{i}: {lista[i][indice]}")
    return

def update(lista, lista_key):
    escolha = forca_opcao("Lista de carnes\n",lista_key)
    indice_item = indices[escolha]
    for i in lista.keys():
        esc = forca_opcao(f"Gostaria de atualizar {i}\n- ",["s","n"])
        if esc == "s":
            novo_valor = input("Digite o novo valor\n-> ")
            lista[i][indice_item] = novo_valor
        else:
            pass
    return

def verifica_numero(msg):
    num = input(msg)
    while not num.isnumeric():
        num = input(msg)
    return int(num)

def comprar():
    item = forca_opcao("Qual item você quer comprar?\n-> ", acougue['Carnes'])
    indice_item = indices[item]
    for key in acougue.keys():
        print|(f"{key}: {acougue[key][indice_item]}")
    continuar = forca_opcao("Você quer continuar? ", ["sim", "não"])
    if continuar == "não":
        return
    qtd = verifica_numero(f"Quantos kg de {item}? ")
    for key in acougue:
    if qtd <= acougue['Estoque'][i]:
        acougue['Estoque'][indice_item] -= qtd
        carrinho['Valor Total'] += qtd*acougue['R$/kg'][indice_item]
        if item not in carrinho['Itens'].keys():
            carrinho['Itens'][item] = qtd
        else:
            carrinho['Itens'][item] += qtd
    else:
        print(f"Só há {acougue['Estoque'][indice_item]}kg no estoque")
        comprar()




acougue = {
    'Carnes': ['Patinho','Colchão Mole','Fraldinha','Picanha','Maminha','Linguiça'],
    'R$/kg': [35.90,49.90,39.90,80.90,45.90,15.00],
    'Estoque': [10,50,30,15,20,100],
    'Validade': ['4','7','5','9','20','8']
}
dic_crud = {
    'opcoes': ['Create','Read','Update','Delete', 'Sair']
}
indices = cria_indice(acougue['Carnes'])

carrinho = {
    "Endereço": {
        "Rua": "",
        "Bairro": "",
        "N°": "",
        "CEP": "",
    },
    "Itens": {},
    "Valor Total": 0,
}
def endereco():
    while True:
        cep = input("Diga seu CEP´: ")
        endereco = requests.get(f"https://viacep.com.br/ws/{cep}/json")
        if endereco.status_code == 200:
            carrinho['Endereço'] = endereco.json()
            carrinho['Endereço']["N°"] = input("Número de residência: ")
            carrinho['Endereço']["Complemento"] = input("Complemento: ")
            break
        else:
            print("Cep inválido")

print("Bem vindo à açougueria Agnello!!!")
usuario = forca_opcao("Você é cliente ou funcionário", ['cliente', 'funcionário'])
while True:
    if usuario == "funcionário":
        operacao = forca_opcao("Qual operação será realizada? ", ["cadastrar", "remover", "atualizar"])
        if operacao == 'cadastrar':
            create()
        elif operacao == "remover":
            delete()
        else:
            update()
        continuar = forca_opcao("Você gostaria de continuar? ", ['sim','não'])
        if continuar == "não":
            break
    else:
        comprar()
        encerrar = forca_opcao("Encerrar compra?", ["sim","não"])
        if encerrar == "sim":
            break

    


import pandas as pd

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

while True:
    print(pd.DataFrame(acougue))
    escolha = forca_opcao("Escolha uma opção\n", dic_crud['opcoes'])

    if escolha == 'Create':
        create(acougue)
        indice = cria_indice()
    elif escolha == 'Read':
        esc = forca_opcao("Lista de carnes\n",acougue['Carnes'])
        indice_esc = acha_indice(acougue['Carnes'],escolha)
        read(acougue,indice_esc)
    elif escolha == 'Update':
        update(acougue, acougue['Carnes'])
    elif escolha == 'Delete':
        delete(acougue)
        indice = cria_indice()
    else:
        break
    


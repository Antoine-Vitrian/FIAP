# defs
def forca_opcao(msg,lista_opcoes):
    msg += '\n'.join(lista_opcoes) + '\n->'
    opcao = input(msg)
    while opcao not in lista_opcoes:
        print("Erro!")
        opcao = input(msg)
    return(opcao)

def acha_indice(lista,elem):
    for i in range(len(lista)):
        if lista[i] == elem:
            return i

def create(lista):
    for key in lista.keys():
        info = input(f"Diga o novo {key}: ")
        lista[key].append(info)
    return lista

def delete(lista, indice):
    for key in lista.keys():
        lista[key].pop(indice)
    return lista

def read(lista,indice):
    for i in lista.keys():
        print(f"{i}: {lista[i][indice]}")
    return

def update():
    pass





acougue = {
    'Carnes': ['Patinho','Colchão Mole','Fraldinha','Picanha','Maminha','Linguiça'],
    'R$/kg': [35.90,49.90,39.90,80.90,45.90,15.00],
    'Estoque': [10,50,30,15,20,100],
    'Validade': ['4','7','5','9','20']
}
dic_crud = {
    'opcoes': ['Create','Read','Update','Delete']
}

escolha = forca_opcao("Escolha uma opção\n-> ", dic_crud['opcoes'])

if escolha == 'Create':
    create(acougue)
elif escolha == 'Read':
    esc = forca_opcao("Lista de carnes",acougue['Carnes'])
    indice_esc = acha_indice(acougue,esc)
    read(indice_esc)
elif escolha == 'Update':
    pass
else:
    


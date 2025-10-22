# Importando Json
import json

# Abre o arquivo fut.json no modo de leitura ('r')
# O 'with open' garante que o arquivo seja fechado automaticamente após o uso
with open('fut.json', 'r') as arquivo:
    # Carrega o conteúdo do arquivo JSON para uma variável Python (dicionário)
    dados = json.load(arquivo)

def forca_opcao(lista, msg):
    escolha = input(msg)
    while escolha not in lista:
        print("Não existe esta opção!!!")
        escolha = input(msg)
    return escolha

# Funções Admin
def acha_indice(lista,elem):
    for i in range(len(lista)):
        if lista[i] == elem:
            return i
        
def cria_indice(lista):
    indices = {}
    for i in range(len(lista)):
        indices[lista[i]] = i
    return indices

# Adicionar algo no Json
def add(lista):
    for key in lista.keys():
        info = input(f"Diga o novo {key}: ")
        lista[key].append(info)
    return

# Deleta algo no Json
def delete(lista, msg, lista_opcoes):
    escolha = forca_opcao(msg, lista_opcoes)
    indice_esc = indices[escolha]
    for key in lista.keys():
        lista[key].pop(indice_esc)
    return

# Edita algo no Json
def edit(lista, lista_key):
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

# Vê algo no Json
def view(lista, indice):
    for i in lista.keys():
        print(f"{i}: {lista[i][indice]}")
    return

# Funções usuário
# Reutilizar funções de ver jogos e noticias

indices = cria_indice(dados['jogo'])
indice_not = cria_indice(dados['noticias'])

contas = ["usuário","administrador"]
menuAdmin = {
    "opções": ["Adicionar", "Deletar", "Editar", "Visualizar", "Sair"]
}
menuUser = {
    "opções": ["Jogos","Notícias","Sair"]
}

menuView = {
    "opções": ["Jogos", "Notícias"]
}

print("Bem vindo ao sistema do Passa Bola!!!")
pessoa = forca_opcao(contas, "Você é usuário ou administrador?\n-> ")

# Área do Usuário
if pessoa == "usuário":
    # Loop principal User
    while True:
        # Mostrando Menu User
        for i in range(len(menuUser["opções"])):
            print(f"{i}.{menuUser['opções'][i]}")
        # Escolha de uma das opções do menu
        opcao = forca_opcao(menuUser["opções"], "Escolha uma das opções\n-> ")
        # Visualização de Jogos
        if opcao == "Jogos":
            for i in range(len(dados['jogos'])):
                print(f"{i}. {dados['jogos'][i]['time_casa']} x {dados['jogos'][i]['time_visitante']}")
            jogo = forca_opcao(indices,"Escolha uma das opções\n-> ")
            view(dados['jogos'], jogo)
        # Visualização de Notícias
        if opcao == "Notícias":
            for i in range(len(dados['noticias'])):
                print(f"{i}. {dados['noticias'][i]['titulo']}")
            noticia = forca_opcao(indice_not,"Escolha uma das opções\n-> ")
            view(dados['noticias'], noticia)
        # Saindo do Programa
        else:
            break

# Área do Administrador
else:
    # Loop principal Admin
    while True:
        indices = cria_indice(dados['jogo'])
        indice_not = cria_indice(dados['noticias'])
        # Mostrando Menu Admin
        for i in range(len(menuAdmin["opções"])):
            print(f"{i}.{menuAdmin['opções'][i]}")
        # Escolha de uma das opções do menu
        opcao = forca_opcao(menuAdmin["opções"], "Escolha uma das opções\n-> ")
        # Método adicionar
        if opcao == "Adicionar":
            add(dados['jogos'])
        # Método deletar
        elif opcao == "Deletar":
            delete()





        # Método editar
        elif opcao == "Editar":
            edit()



            
        # Método visualizar
        elif opcao == "Visualizar":
            opcao = forca_opcao(menuView["opções"], "Escolha uma das opções\n-> ")
            # Visualização de Jogos
            if opcao == "Jogos":
                for i in range(len(dados['jogos'])):
                    print(f"{i}. {dados['jogos'][i]['time_casa']} x {dados['jogos'][i]['time_visitante']}")
                jogo = forca_opcao(indices,"Escolha uma das opções\n-> ")
                view(dados['jogos'], jogo)
            # Visualização de Notícias
            else:
                for i in range(len(dados['noticias'])):
                    print(f"{i}. {dados['noticias'][i]['titulo']}")
                noticia = forca_opcao(indice_not,"Escolha uma das opções\n-> ")
                view(dados['noticias'], noticia)
        # Saindo do Programa
        else:
            break

print("Saindo do programa...")
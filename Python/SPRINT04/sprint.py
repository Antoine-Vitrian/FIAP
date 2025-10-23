# Importando Json
import json

# Abre o arquivo fut.json no modo de leitura ('r')
with open(r"C:\Users\victo\FIAP\Python\SPRINT04\fut.json", 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

# ------------------ Funções de entrada ------------------

def forca_opcao(lista, msg):
    escolha = input(msg)
    while escolha not in lista:
        print("❌ Não existe esta opção!")
        escolha = input(msg)
    return escolha

def forca_opcao_int(msg, limite):
    """Força o usuário a digitar um número inteiro dentro do intervalo."""
    while True:
        try:
            escolha = int(input(msg))
            if 0 <= escolha < limite:
                return escolha
            else:
                print("❌ Índice fora do intervalo!")
        except ValueError:
            print("❌ Por favor, digite um número válido!")

# ------------------ Funções de utilidade ------------------

def cria_indice(lista, chave):
    """Cria um dicionário de índices baseado em um campo do JSON."""
    indices = {}
    for i, item in enumerate(lista):
        indices[i] = item[chave]
    return indices

# ------------------ Funções Admin ------------------

def add(lista):
    """Adiciona um novo item a uma lista de dicionários."""
    novo_item = {}
    for key in lista[0].keys():
        info = input(f"Diga o novo {key}: ")
        novo_item[key] = info
    lista.append(novo_item)
    print("✅ Item adicionado com sucesso!")

def delete(lista):
    """Remove um item da lista baseado no índice."""
    for i, item in enumerate(lista):
        print(f"{i}. {list(item.values())[0]}")  # Mostra o primeiro campo como identificador
    indice = forca_opcao_int("Digite o índice do item que deseja excluir: ", len(lista))
    removido = lista.pop(indice)
    print(f"🗑️  Item removido: {removido}")

def edit(lista):
    """Edita um item da lista baseado no índice."""
    for i, item in enumerate(lista):
        print(f"{i}. {list(item.values())[0]}")
    indice = forca_opcao_int("Digite o índice do item que deseja editar: ", len(lista))

    print("Digite os novos valores (pressione Enter para manter o valor atual):")
    for key in lista[indice].keys():
        novo_valor = input(f"{key} ({lista[indice][key]}): ")
        if novo_valor.strip():
            lista[indice][key] = novo_valor

    print("✏️  Item atualizado com sucesso!")

def view(lista, indice):
    """Mostra as informações completas de um item da lista."""
    item = lista[indice]
    print("📰 Detalhes:")
    for chave, valor in item.items():
        print(f"{chave}: {valor}")
    print()

# ------------------ Menus ------------------

contas = ["usuário", "administrador"]

menuAdmin = {
    "opções": ["Adicionar", "Deletar", "Editar", "Visualizar", "Sair"]
}

menuUser = {
    "opções": ["Jogos", "Notícias", "Sair"]
}

menuView = {
    "opções": ["Jogos", "Notícias"]
}

# ------------------ Execução principal ------------------

print("⚽ Bem-vindo ao sistema do Passa Bola!!! ⚽")
pessoa = forca_opcao(contas, "Você é usuário ou administrador?\n-> ")

# Área do Usuário
if pessoa == "usuário":
    while True:
        print("\n--- MENU USUÁRIO ---")
        for i, opcao in enumerate(menuUser["opções"]):
            print(f"{i}. {opcao}")

        opcao = forca_opcao(menuUser["opções"], "Escolha uma opção (digite o nome):\n-> ")

        if opcao == "Jogos":
            print("\n=== JOGOS ===")
            for i, jogo in enumerate(dados['jogos']):
                print(f"{i}. {jogo['time_casa']} x {jogo['time_visitante']}")
            jogo = forca_opcao_int("Escolha um jogo pelo índice:\n-> ", len(dados['jogos']))
            view(dados['jogos'], jogo)

        elif opcao == "Notícias":
            print("\n=== NOTÍCIAS ===")
            for i, noticia in enumerate(dados['noticias']):
                print(f"{i}. {noticia['titulo']}")
            noticia = forca_opcao_int("Escolha uma notícia pelo índice:\n-> ", len(dados['noticias']))
            view(dados['noticias'], noticia)

        else:
            break

# Área do Administrador
else:
    while True:
        print("\n--- MENU ADMIN ---")
        for i, opcao in enumerate(menuAdmin["opções"]):
            print(f"{i}. {opcao}")

        opcao = forca_opcao(menuAdmin["opções"], "Escolha uma opção (digite o nome):\n-> ")

        if opcao == "Adicionar":
            tipo = forca_opcao(menuView["opções"], "Quer adicionar em Jogos ou Notícias?\n-> ")
            if tipo == "Jogos":
                add(dados['jogos'])
            else:
                add(dados['noticias'])

        elif opcao == "Deletar":
            tipo = forca_opcao(menuView["opções"], "Quer deletar em Jogos ou Notícias?\n-> ")
            if tipo == "Jogos":
                delete(dados['jogos'])
            else:
                delete(dados['noticias'])

        elif opcao == "Editar":
            tipo = forca_opcao(menuView["opções"], "Quer editar em Jogos ou Notícias?\n-> ")
            if tipo == "Jogos":
                edit(dados['jogos'])
            else:
                edit(dados['noticias'])

        elif opcao == "Visualizar":
            tipo = forca_opcao(menuView["opções"], "Quer ver Jogos ou Notícias?\n-> ")
            if tipo == "Jogos":
                print("\n=== JOGOS ===")
                for i, jogo in enumerate(dados['jogos']):
                    print(f"{i}. {jogo['time_casa']} x {jogo['time_visitante']}")
                jogo = forca_opcao_int("Escolha um jogo pelo índice:\n-> ", len(dados['jogos']))
                view(dados['jogos'], jogo)
            else:
                print("\n=== NOTÍCIAS ===")
                for i, noticia in enumerate(dados['noticias']):
                    print(f"{i}. {noticia['titulo']}")
                noticia = forca_opcao_int("Escolha uma notícia pelo índice:\n-> ", len(dados['noticias']))
                view(dados['noticias'], noticia)

        else:
            break

# ------------------ Salvando alterações ------------------

with open(r"C:\Users\victo\FIAP\Python\SPRINT04\fut.json", 'w', encoding='utf-8') as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False, indent=4)

print("👋 Saindo do programa... Alterações salvas com sucesso!")

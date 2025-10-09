# import requests

# import pandas as pd
# acougue = {
#     'Carnes' : ['Patinho','Coxão Mole','Fraldinha','Picanha','Maminha','LINGÜIÇA'],
#     'Preço/kg' : [35.90,49.90,39.90,80.00,45.90,15],
#     'Estoque' : [10,50,30,15,20,100],
#     'Validade' : ['4','7','5','9','20','50']
# }
# def forca_opcao(msg,lista_opcoes):
#     opcoes = '\n'.join(lista_opcoes)
#     opcao = input(f"{msg}\n{opcoes}\n->")
#     while not opcao in lista_opcoes:
#         print("Inválido!")
#         opcao = input(f"{msg}\n{opcoes}\n->")
#     return opcao

# def cria_indices():
#     global indices
#     indices = {}
#     for i in range(len(acougue['Carnes'])):
#         indices[acougue['Carnes'][i]] = i
#     return indices

# def cadastrar():
#     global indices
#     for key in acougue.keys():
#         info = input(f"Diga o novo {key}: ")
#         acougue[key].append(info)
#     print(pd.DataFrame(acougue))
#     indices = cria_indices()
#     return

# def remover():
#     global indices
#     item = forca_opcao("Qual item será removido?",acougue['Carnes'])
#     indice_item = indices[item]
#     for key in acougue.keys():
#         acougue[key].pop(indice_item)
#     indices = cria_indices()
#     return

# def atualizar():
#     item = forca_opcao("Qual item você deseja atualizar?",acougue['Carnes'])
#     indice_item = indices[item]
#     keys = list(acougue.keys())
#     keys.pop(0)
#     for key in keys:
#         if forca_opcao(f"Você quer atualizar {key} para {item}?",['sim','não']) == 'sim':
#             info = input(f"Diga o novo {key}: ")
#             acougue[key][indice_item] = info
#     print(pd.DataFrame(acougue))
#     return

# def verifica_numero(msg):
#     num = input(msg)
#     while not num.isnumeric():
#         num = input(msg)
#     return int(num)

# def comprar():
#     item = forca_opcao("Qual item você quer comprar?",acougue['Carnes'])
#     indice_item = indices[item]
#     for key in acougue.keys():
#         print(f"{key} : {acougue[key][indice_item]}")
#     continuar = forca_opcao(f"Você quer levar {item}?",['SIM','não'])
#     if continuar == 'não':
#         return
#     qtd = verifica_numero(f"Quantos kg de {item}?")
#     if qtd <= acougue['Estoque'][indice_item]:
#         acougue['Estoque'][indice_item] -= qtd
#         carrinho['Valor Total'] += qtd*acougue['Preço/kg'][indice_item]
#         if item not in carrinho['Itens'].keys():
#             carrinho['Itens'][item] = qtd
#         else:
#             carrinho['Itens'][item] += qtd
#     else:
#         print(f"Só há {acougue['Estoque'][indice_item]}kg no estoque!")
#         comprar()

# def cadastro_endereco():
#     while True:
#         cep = input("Diga seu cep: ")
#         endereco = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
#         if endereco.status_code == 200:
#             carrinho['Endereço'] = endereco.json()
#             carrinho['Endereço']['Nº'] = input("Numero da residencia: ")
#             carrinho['Endereço']['Complemento'] = input("Complemento: ")
#             break
#         else:
#             print("Cep Inválido")
#     return


# indices = cria_indices()
# carrinho = {
#     "Endereço" : {
#         "Rua" : '',
#         "Bairro" : '',
#         'Nº' : '',
#         "Cep" : ''
#     },
#     "Itens" : {},
#     "Valor Total": 0
# }

# print("BEM VINDO À AÇOUGUERIA AGNELLO!!!!👌😘👍🙌😁😒🍖🐏")
# usuario = forca_opcao("Você é",['cliente','funcionário'])
# while True:
#     if usuario == 'funcionário':
#         operacao = forca_opcao("Qual operação será realizada?",['cadastrar','remover','atualizar'])
#         if operacao == 'cadastrar':
#             cadastrar()
#         elif operacao == 'remover':
#             remover()
#         else:
#             atualizar()
#         continuar = forca_opcao("Você deseja realizar outra operação?",['sim','nao'])
#         if continuar == 'não':
#             break
#     else:
#         cadastro_endereco()
#         comprar()
#         encerrar = forca_opcao("Encerrar a compra ou ver mais itens?",['encerrar', 'continuar'])
#         if encerrar == 'encerrar':
#             print(carrinho)
#             break





# while True:
#     try:
#         a = int(input("Digite um número\n-> "))
#         break
#     except:
#         print("Valor inválido!!!")


# while True:
#     try:
#         a = int(input("Diga um número: "))
#         b = int(input("Diga outro número: "))
#         print(a/b)
#         lista = [1,2]
#         print(lista[3])
#     except ValueError:
#         print("Digita um número!!!")
#     except ZeroDivisionError:
#         print("Não dá para dividir por zero!!!")
#     except Exception as e:
#         print(f"algo deu errado!!! {e}")
#     else:
#         print("oi")



# lista = [5,8,1,7,9,4]
# while True:
#     try:
#         print(lista)
#         i = int(input("Digite um índice da lista: "))
#         print(lista[i])
#     except IndexError:
#         print("Índice inexistente!!!")
#     except ValueError:
#         print("Apenas números podem ser digitados!!!")
#     else:
#         print("Parabéns, você sairá do loop")
#         break


# try:
#     mensagem = "inteiro"
#     a = int(input("Digite um número inteiro: "))
#     mensagem = "flutuante"
#     b = int(input("Digite um número flutuante: "))
# except ValueError:
#         print(f"Digite um número {mensagem}!!")    



# def acha_indice(lista, elem):
#     for i in range(len(lista)):
#         if lista[i]:
#             return i
#     raise ValueError(f"Não achei o {elem}")







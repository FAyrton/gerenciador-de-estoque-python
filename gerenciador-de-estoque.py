from time import sleep
import os

user_cad = {
    "450": "felipe1278",
    "332": "nicolly50",
    "781": "pedro123"
}

permissoes = {
    "450": 5,
    "332": 5,
    "781": 1
}

estoque = {
    "cadeiras": 4000,
    "ventiladores": 3500,
    "sofás": 600
}

user_tela = input('Digite seu nome de tela: ').capitalize()
def checar_login(user_cad):
    id = input('Digite seu ID: ')
    if id in user_cad:
        senha = input('Digite sua senha: ')
        os.system('cls')
        print('Usuário Acessado \nValidando senha...')
        sleep(3.8)
        senha_correta = user_cad[id]
        if senha == senha_correta:
            os.system('cls')
            print('Senha Validada \nAcessando sistema.')
            sleep(5)
            return True
        else:
            os.system('cls')
            print('Senha Inválida \nEncerrando programa.')
            sleep(5)
            return False
    else:
        print('Usuário Não Encontrado. \nTente Novamente.')
def adicionar_item(estoque):
    os.system('cls')
    item_nome = input('Que item deseja adicionar? ').strip().lower()
    if item_nome in estoque:
        os.system('cls')
        print('Item já existente no estoque. Digite quantidade a atualizar: ')
        try:
            item_valor = int(input())
        except ValueError:
            print('Valor Inválido. Tente novamente.')
            return False
        estoque[item_nome] += item_valor
        print('Item Atualizado com Sucesso!')
        print('----------')
        print(estoque)
        sleep(5)
    else:
        try:
            item_valor = int(input('Digite o valor a adicionar: '))
        except ValueError:
            print('Valor Inválido. \nTente Novamente.')
            return False
        estoque[item_nome] = item_valor
        print('Item Adicionado com Sucesso! \nExibindo Estoque...')
        sleep(3.5)
        print(estoque)
        print('--------')
        input('Pressione ENTER para continuar...')
def remover_item(estoque):
    print(estoque)
    print('----------')
    item_nome = input('Qual item deseja remover? ')
    if item_nome not in estoque:
        print('Item Não Encontrado...')
    else:
        estoque.pop(item_nome)
        print('Item Removido com Sucesso!')
        sleep(5)
        print(estoque)
        print('--------')
        input('Pressione ENTER para continuar...')
        return estoque
def cadastrar_user(user_cad, permissoes):
    id = input('Por Favor, digite novamente seu ID: ')
    os.system('cls')
    print('Verificando seu nível de permissão...')
    sleep(5)
    if id in permissoes and permissoes[id] >= 5:
        print('Permissão Concedida.')
        sleep(3.5)
        new_id = input('Defina novo ID (Limite de 3 Dígitos): ')
        if new_id in user_cad:
            print('Usuário Já Existente.')
        else:
            new_pass = input('Defina nova Senha: ')
            if len(new_id) > 3:
                print('ID Inválido. Digite Apenas 3 Dígitos.')
            else:
                user_cad[new_id] = new_pass
                permissoes[new_id] = 1
                print('Usuário Cadastrado com Sucesso!')
                sleep(3.9)
                print('----------')
                print(user_cad)
                print('----------')
                print(permissoes)
                print('----------')
                input('Pressione ENTER para continuar...')
                return user_cad


    elif id not in permissoes:
        print('ID Não Encontrada. \nTente Novamente.')
    else:
        print('Nível de Permissão Inferior.')
        sleep(3.5)

check = checar_login(user_cad)

if check:
    while True:
        print('----------')
        print(f'Olá, {user_tela}! \nO que deseja fazer?')
        escolha = input('[1] - Adicionar Item \n[2] - Remover Item \n[3] - Ver Estoque' \
        '\n[4] - Cadastrar Usuário \n[5] - Encerrar Programa \n---------- \n')

        if escolha == '1':
            adicionar_item(estoque)
            os.system('cls')
        
        elif escolha == '2':
            remover_item(estoque)
            os.system('cls')
        
        elif escolha == '3':
            print(estoque)

        elif escolha == '4':
            cadastrar_user(user_cad, permissoes)
            os.system('cls')


        elif escolha == '5':
            print('Encerrando Programa...')
            sleep(4)
            os.system('cls')
            print(f'Até a Próxima, {user_tela}!')
            break

else:
    print('Login Inválido. \nTente Novamente.')
    


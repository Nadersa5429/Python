usuarios = ['Bruno', 'Guilherme']
def create():
    novo_usuario = input('digite o nome do novo usuario: ')
    usuarios.append(novo_usuario)
    print('Usuário {} cadastrado com sucesso!'.format(novo_usuario))
def read():
    print('Usuários cadastrados:')
    for i, usuario in enumerate(usuarios, start=1):
        print(f'{i}. {usuario}')
def update():
    read()
    indice = int(input('digite o número do usuário que deseja atualizar: '))
    if 0 <= indice < len(usuarios):
        novo_nome = input('digite o novo nome para {usuarios[indice]}: ')
        usuarios[indice] = novo_nome
        print(f'Usuário atualizado para {novo_nome} com sucesso')
    else:
        print('Usuário inválido.')
def delete():
    read()
    indice = int(input('digite o número do usuário que deseja excluir: '))
    if 0 <= indice < len(usuarios):
        removido = usuarios.pop(indice)
        print(f'usuário {removido} excluído com sucesso!')
    else:
        print('usuário inválido.')
def menu():
    opcao = 0
    while opcao != 5:
        print('\nEscolha uma opção:')
        print('1 - Cadastrar Usuario')
        print('2 - ler usuarios')
        print('3 - atualizar usuario')
        print('4 - deletar usuario')
        print('5 - sair do programa')

        opcao=int(input('escolha a opção desejada: '))

        if opcao == 1:
            create()
        elif opcao == 2:
            read()
        elif opcao == 3:
            update()
        elif opcao == 4:
            delete()
        elif opcao == 5:
            exit()
        else:
            print('opção invalida')
menu()

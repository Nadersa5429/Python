class UsuarioSistema:
    usuarios = []

    @classmethod
    def create(cls):
        novo_usuario = input('Digite o nome do novo usuário:')
        cls.usuarios.append(novo_usuario)
        print(f'Usuário {novo_usuario} cadastrado com sucesso!')
    @classmethod
    def read(cls):
        print('Usuários cadastrados:')
        for i, usuario in enumerate(cls.usuarios, start=1):
            print(f'{i}. {usuario}')
    @classmethod
    def update(cls):
        cls.read()
        indice = int(input('Digite o número do usuário que deseja atualizar: ')) - 1
        if 0 <= indice < len(cls.usuarios):
            novo_nome = input(f'Digite o novo nome para {cls.usuarios[indice]}: ')
            print(f'Usuário atualizado para [novo_nome] com sucesso!')
        else:
            print('Usuário inválido.')
    @classmethod
    def delete(cls):
        cls.delete()
        indice = int(input('Digite o número do usuário que deseja atualizar: ')) - 1
        if 0 <= indice < len(cls.usuarios):
            removido = cls.usuarios.pop(indice)
            print(f'Usuário {removido} excluído com sucesso')
        else:
            print('Usuário inválido.')
    def menu():
        opcao = 0
        while opcao != 5:
            print('''Escolha uma opção:
            [ 1 ] Cadastrar Usuário
            [ 2 ] Ler Usuários
            [ 3 ] Atualizar Usuário
            [ 4 ] Deletar Usuário
            [ 5 ] Sair do programa''')

            opcao = int(input('Digite o número da opção desejada: '))
            if opcao == 1:
                UsuarioSistema.create()
            elif opcao == 2:
                UsuarioSistema.read()
            elif opcao == 3:
                UsuarioSistema.update()
            elif opcao == 4:
                UsuarioSistema.delete()
            elif opcao == 5:
                print('Saindo do programa.')
            else:
                print('Opção inválida. Tente novamente.')
    menu()

cliente_usuario = []
cliente_senha = []

def gerenciador_usuarios():
    while True:
        print('Menu: ')
        print('1. Criar usuário')
        print('2. Remover usuário')
        print('3. Login')
        print('4. Sair')
        escolha = input('Escolha uma das opções: ')

        if escolha == '1':
            usuario_login = input('Crie um nome de usuário: ')
            while usuario_login in cliente_usuario:
                print('Nome de usuário já existe. Tente outro.')
                usuario_login = input('Crie um nome de usuário: ')
            senha_login = input('Crie uma senha: ')
            while len(senha_login) < 6:
                print('A senha deve ter pelo menos 6 caracteres. Tente novamente.')
                senha_login = input('Crie uma senha: ')
            cliente_usuario.append(usuario_login)
            cliente_senha.append(senha_login)
            print('Usuário criado com sucesso.')

        elif escolha == '2':
            remover_usuario = input('Digite o nome do usuário a ser removido: ')
            if remover_usuario in cliente_usuario:
                index = cliente_usuario.index(remover_usuario)
                cliente_usuario.pop(index)
                cliente_senha.pop(index)
                print('Usuário removido com sucesso.')
            else:
                print('Usuário não encontrado.')

        elif escolha == '3':
            login(cliente_usuario, cliente_senha)

        elif escolha == '4':
            break

        else: 
            print('Opção inválida, tente novamente.')
    
    return cliente_usuario, cliente_senha

def login(cliente_usuario, cliente_senha):
    if not cliente_usuario:
        print("Nenhum usuário cadastrado. Cadastre um usuário primeiro.")
        return 

    usuario = input('Digite seu nome de usuário: ')
    while usuario  not in cliente_usuario:
        print('Usuario não encontrado. tente novamente.')
        usuario = input('Digite seu nome de usuário: ')
    index = cliente_usuario.index(usuario)
    senha = input('digite sua senha: ')    
    while senha != cliente_senha[index]:
        print('Senha incorreta. Tente novamente.')
        senha= input('Digite sea senha: ')

    print('Acesso concedido. Seja bem vindo.')

# Iniciando o gerenciador de usuários
resultado = gerenciador_usuarios()
print('Usuários: ', resultado[0])
print('Senhas: ', resultado[1])

def cadastrar_livros( ):
      biblioteca = []
      while True:
         livro = input('digite o nome  do livro (ou digite "sair" para terminar): ')
         if livro.lower() == 'sair':
           break
         biblioteca.append(livro)
      return biblioteca
def procurar_livro(biblioteca):
    livro_procurado = input('Digite o livro que você deseja proucurar. ')
    if livro_procurado in biblioteca:
        index = biblioteca.index(livro_procurado)
        print(f'Livro {livro_procurado} na posição {index}')
    else:
       print('livro não encontrado.')
def gerenciador_livros():
    biblioteca = cadastrar_livros()
    print('livros cadastrados', biblioteca)
    while True:
        print('menu')
        print('1 prcurar livros')
        print('2 sair')
        escolha = input('escolha uma das opções:')

        if escolha == '1':
            procurar_livro(biblioteca)
        elif escolha == '2':
            break
        else:
            print('Opção invalida, tente novamente.')
def main():      
    gerenciador_livros()
  
if __name__ =="__main__":
    main()

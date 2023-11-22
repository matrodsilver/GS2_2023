# Opções de Dados
def Perguntar():
    resposta = input("\nO que deseja consultar?\n" +
                     "<U> - Para ir à aba de Usuários\n" +
                     "<D> - Para ir à aba de Dados\n").upper()
    return resposta

def Dados():
    resposta = input("\nO que deseja consultar?\n" +
                     "<C> - Para ir à aba de consultas\n" +
                     "<V> - Para ir à aba de verificação dos Dados\n").upper()
    return resposta

def Consulta(usuarios):
    pass#with open("agendamentos.txt", "a")

def Verificacao(usuarios):
    print("verificação")

# Opções de Usuário
def Usuario():
    resposta = input("\nO que deseja realizar?\n" +
                     "<I> - Para Inserir um usuário\n" +
                     "<P> - Para Pesquisar um usuário\n" +
                     "<E> - Para Excluir um usuário\n" +
                     "<L> - Para Listar usuários\n").upper()
    return resposta

def Inserir(usuarios):
    chave = input("Digite o CPF:\n")
    usuarios[chave] = [input("Digite uma senha: \n"),
                                 input("Digite o número de um tipo de credencial (Paciente (1) | Profissional da saúde (2) | Responsável legal (3)): \n"),
                                 input("Digite o nome: \n"),
                                 input("Digite a última data de acesso: \n"),
                                 input("Qual a última estação acessada: \n")]
    with open("usuarios.txt", "a") as registru:  # regitro em arquivo
        string = chave

        for var in usuarios[chave][1:]:
            string += f',{var}'

        registru.write(string + "\n")

def Pesquisar(usuarios):
    cargo = ''
    
    cpf = input("Digite o CPF do usuário: \n")

    print(usuarios[cpf][1])

    match usuarios[cpf][1]:
        case "1":
            cargo = "Paciente"
        case "2":
            cargo = "Profissional da saúde"
        case "3":
            cargo = "Responsável legal"

    print(f'''{cargo}: {usuarios[cpf][2]}
Última data acessada: {usuarios[cpf][3]}
Última estação acessada: {usuarios[cpf][4]}
          ''')

def Listar(usuarios):
    for usuario in usuarios:
        print("◉", usuarios[usuario][2])

def Excluir(usuarios):
    lista = []
    cpf = input("Digite o CPF do usuário a ser excluído: \n")

    nome = usuarios[cpf][2]

    with open("usuarios.txt", "r") as registru:
        for linha in registru.readlines():
            if (cpf + str(usuarios[cpf]) + "\n") != linha:
                print(cpf + str(usuarios[cpf]) + "\n")
                print(linha)
                lista.append(linha)

        del usuarios[cpf] # ou -> usuários.pop(nome)
        # del linha-> num dá

    with open("usuarios.txt", "w") as registru:
        for elemento in lista:
            registru.write(elemento)
    print(nome, "excluído com sucesso")
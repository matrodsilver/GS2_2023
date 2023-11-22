def Usuario():
    resposta = input("\nO que deseja realizar?\n" +
                     "<I> - Para Inserir um usuário\n" +
                     "<P> - Para Pesquisar um usuário\n" +
                     "<E> - Para Excluir um usuário\n" +
                     "<L> - Para Listar usuários\n").upper()
    return resposta


def Inserir(dicionario):
    chave = input("Digite o CPF:\n")
    dicionario[chave] = [input("Digite uma senha: \n"),
                                 input("Digite o número de um tipo de credencial (Paciente (1) | Profissional da saúde (2) | Responsável legal (3)): \n"),
                                 input("Digite o nome: \n"),
                                 input("Digite a última data de acesso: \n"),
                                 input("Qual a última estação acessada: \n")]
    with open("dados.txt", "a") as registru:  # regitro em arquivo
        string = chave

        for var in dicionario[chave][1:]:
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
        print(usuario)


def Excluir(usuarios):
    lista = []
    nome = input("Digite o login do usuário a ser excluído: \n")
    with open("dados.txt", "r") as registru:
        for linha in registru.readlines():
            if (nome + str(usuarios[nome]) + "\n") != linha:
                lista.append(linha)
                with open("dados.txt", "w") as registru:
                    for elemento in lista:
                        registru.write(elemento)
                # del linha-> num dá
    del usuarios[nome]  # ou -> usuários.pop(nome)
    print(nome, "excluído com sucesso")
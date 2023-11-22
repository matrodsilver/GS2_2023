from acesso import *  # Só script °-°

usuarios = {}

with open("usuarios.txt", "r") as registru:
        for linha in registru.readlines():
             usuarios[str(linha[:11])] = linha[11:-1].split(",")
             
print(usuarios)

escolha = Perguntar()

while escolha == "U" or escolha == "D":
    if escolha == "U":
        opcao = Usuario()

        if opcao == "I":
            Inserir(usuarios)
        elif opcao == "P":
            Pesquisar(usuarios)
        elif opcao == "L":
            Listar(usuarios)
        elif opcao == "E":
            Excluir(usuarios)

    elif escolha == "D":
        opcao = Dados()
        
        if opcao == "C":
            Consulta(usuarios)
        elif opcao == "V":
            Verificacao(usuarios)
    
    escolha = Perguntar()

print(usuarios)
# print(usuarios.keys())
# print(usuarios.values())
# usuarios.clear()
# print(usuarios)
# usuarios.pop(input("\nlogin.pop():").upper())
# print(usuarios)
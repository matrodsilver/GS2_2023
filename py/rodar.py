from acesso import *  # Só script °-°

usuarios = {}

with open("usuarios.txt", "r") as registru:
        for linha in registru.readlines():
             usuarios[str(linha[:11])] = linha[11:-1].split(",")
             
print(usuarios)

opcao = Perguntar()

while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":
        Inserir(usuarios)
    elif opcao == "P":
        Pesquisar(usuarios)
    elif opcao == "L":
        Listar(usuarios)
    elif opcao == "E":
        Excluir(usuarios)
    opcao = Perguntar()

print(usuarios)
# print(usuarios.keys())
# print(usuarios.values())
# usuarios.clear()
# print(usuarios)
# usuarios.pop(input("\nlogin.pop():").upper())
# print(usuarios)
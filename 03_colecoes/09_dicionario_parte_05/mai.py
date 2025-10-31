# biblioteca
import os

# declaracao de lista
usuarios = []

os.system("cls")

while True:
    # menu
    print("1 - cadastrar novo usuario")
    print("2 - exibir usuario")
    print("3 - sair do programa")
    opcao = input("Informe a opcao desejada:").strip()

    os.system("cls")

    match opcao:
        case "1":
            usuario = {}
            usuario['nome'] = input("Informe um novo usuario:").strip().title()
            usuario['idade'] = int(input("Informe a idade do usuario:").strip())
            usuario['email'] = input("Informe o email do usuario:").strip().lower()
            usuarios.append(usuario)
            os.system("cls")
            print("Novo usuario inserido com sucesso.")
        case "2":
            for usuario in usuarios:
                for chave in usuario:
                    print(f"{chave.capitalize()}: {usuario[usuario]}")
                print(f"{'-'*40}")
        case "3":
            break
        case _:
            print("opção invalida, tente novamente.")
            continue

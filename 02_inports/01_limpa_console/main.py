# importacao de bibliotecas
import os

#loop

while True:
    #limpa console
    os.system("cls")

    # tratamentdo de excecao
    try:
        nome = input("informe seu nome: ").strip().title()
        email = input("informe seu email: ").strip().lower()
        cpf = input("informe seu CPF: ").strip()

        # impeza de console
        os.system("cls")
        
        # saida de dados
        print(f"Nome: {nome}")
        print(f"E-mail: {email}")
        print(f"CPF: {cpf}")

        # menu:
        print("1 - Inserir novos dados. ")
        print("2 - Sair do programa. ")

        opcao = input("Opção desejada: ").strip()

        # verifica a opcao escolhida
        match opcao:
            case "1":
                continue
            case "2":
                print("programa encerrado ")
                break
            case _:
                print("opção inválida. Tente novamente. ")
                break
    except:
        print("Não foi possivel receber informações. Tente novamente mais tarde")
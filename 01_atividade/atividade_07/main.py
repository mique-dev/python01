# biblioteca
import os

# limpar tela
def limpar():
    os.system("cls" if os .name == "nt" else "clear")

# minha biblioteca
from classes import banco

def main():
    usuario = banco(nome="",cpf="", depositar="", sacar="", saldo="")

# menu
while True:
    limpar()
    print("Bem vindo ao banco")
    print("1 - Inserir os dados da conta")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Saldo")
    print("5 - Sair")
    opcao = input("Digite uma opção para prosseguir: ")
    
    match opcao:
        case "1":
            limpar()
            tiular = input("Informe o nome do titular: ").strip().title()
            saldo = float(input("Informe o saldo da conta: ").strip().replace(",", "."))
            cpf = input("Informe o CPF do titular: ").strip()
            numero_da_agencia = input("Informe o numero da agencia: ").strip()
            numero_da_conta = input("Informe o numero da conta: ").strip()
            continue
        case "2":
            depositar = float(input("Informe o valor que deseja depositar: ").strip().replace(",", "."))
            banco.depositar(depositar)
            continue
        case "3":
            sacar = float(input("Informe o valor que deseja sacar: ").strip().replace(",", "."))
            banco.sacar(sacar)
            continue
        case "4":
            banco.saldo()
            continue
        case "5":
            limpar()
            print("Obrigado por usar nosso banco") 
            break
        case _:
            limpar()
            print("Opção inválida")
            continue


if __name__ == "__main__":
    main()
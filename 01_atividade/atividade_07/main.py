import os
from classes import Conta
def limpar ():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    limpar()

    cc = Conta(titular ="", cpf ="", n_agencia ="7462-2", n_conta ="8787-9", saldo ="")

    cc.titular = input("Informe seu nome: ").strip().title()
    cc.cpf = input("Informe seu CPF: ").strip()

    while True:
        print("1 - Consultar dados da conta")
        print("2 - Depositar valor")
        print("3 - Sacar valor")
        print("4 - Sair do programa")
        opcao = input("Informe a opção desejada: ").strip()
        match opcao:
            case "1":
                cc.consultar_dados()
                continue
            case "2":
                valorr = float(input("Informe o valor que deseja depositar: R$").strip().replace(",","."))
                print(f"Deposito realizado com sucesso. Seu saldo atual é de R${cc.depositar(valor):.2F}")
            case "3":
                valor = float(input("Informe o valor que deseja sacar: R$").strip().replace(",","."))
                print(f"Valor sacado: R${cc.sacar(valor):.2F}")
                continue
            case "4":
                print("Programa emcerrado")
                break
            case _:
                print("Opção inválida")
                continue

if __name__ == "__main__":
    main()
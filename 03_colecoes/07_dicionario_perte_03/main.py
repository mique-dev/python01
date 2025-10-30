# biblioteca
import os

os.system("cls")

# declaracao de dicionario
veiculo = {'fabricante': "chevrolet", 'modelo': "Chevette", 'ano': 1973, 'cor': "branco", 'placa': "ab-1973"}

# exibe os dados
for chave in veiculo:
    print(f"{chave.capitalize()}: {veiculo[chave]}")

# usuario ecolhe o campo que deseja mudar
while True:
    campo = input("informe o campo que deseja alterar ou digite 'sair' para finalizar): ").strip().lower()

    match campo:
        case "fabricante":
            veiculo["fabricante"] =input("Informe o novo valor do fabricante").striP()
        case "modelo":
            veiculo["modelo"] =input("Informe o novo valor do modelo").strip()
        case "ano":
            veiculo["ano"] =int(input("Informe o novo valor do ano").strip())
        case "cor":
            veiculo["cor"] =input("Informe o novo valor da cor").strip()
        case "placa":
            veiculo["placa"] =input("Informe o novo valor da placa").strip()
        case "sair":
            break
        case _:
            print("valor inválodo")
            continue
    # mostra na tela os novos valores
    for chave in veiculo:
        print(f"{chave.capitalize()}: {veiculo[chave]}")
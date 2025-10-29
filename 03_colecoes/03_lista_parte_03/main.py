# bibliotecas
import os
import time

# declaração de lista
nomes = []

os.system("cls")

# loop
while True:
    # menu 
    print("1 - inserir nome na lista")
    print("2 - exibir lista de nomes")
    print("3 - excluir nome da lista")
    print("4 - sair do programa")
    opcao = input("Informe a opção desejada: ").strip()
    match opcao:
        case "1":
            os.system("cls")
            novo_nome = input("Insira novo nome na lista:").strip().title()
            nomes.append(novo_nome)
            os.system("cls")
            print(f"{novo_nome} inserido na lista.")
            continue
        case "2":
            os.system("cls")
            print("exibir lista de nomes:")
            for i in range(len(nomes)):
                print(f"{i} - {nomes[i]}")
            print(f"\n{'-'*40}\n")
            continue
        case "3":
            try:
                posicao = int(input("Informe a posição do nome a ser excluído: ").strip())
                if posicao >= 0 and posicao < len(nomes):
                    del(nomes[posicao])
                    print(f"Nome excluido com sucesso.")
                else:
                    print(f"Posicao inexistente")
            except Exception as e:
                print(f"Posição inválida. {e}")
            continue
        case "4":
            print("Sair do programa: ")
            break
        case "_":
            print("Opção inválida. ")
            continue


# declaracao de lista
nomes = []

try:
    while True:
        print("1 - inserir nome na lista")
        print("2 - exibir lista")
        print("3 - sair do programa")
        opcao = input("Informe a opção desejada: ").strip()
        match opcao:
            case "1":
                novo_nome = input("Informe o nome: ").strip().title()
                nomes.append(novo_nome)
                print(f"{novo_nome} inserido com sucesso na lista> ")
            case "2":
                print("\nLista de nomes:\n")
                for nome in nomes:
                    print(nome)
            case "3":
                break
            case _:
                print("Opção inválida. Tente novamente.")
                continue
except Exception as e:
    print(f"cartão recusado. {e}.")
finally:
    print("programa encerrado.")
# loop
while True:
    try:
        # menu
        print("1 - soma")
        print("2 - subtração")
        print("3 - multiplicação")
        print("4 - divisão")
        print("5 - sair do programa")
        opcao = input("informe a opção desejada:").strip()

        if opcao != "5":
            n1 = int(input("informe o 1º valor: ").strip())
            n2 = int(input("informe o 2º valor: ").strip())

            match opcao:
                case "1":
                    result = n1+n2
                    print(f" o numero da soma é {result}")
                    continue
                case "2":
                    result = n1-n2
                    print(f"o resultado da subtração é {result}")
                    continue
                case "3":
                    result(f"o resultado da multiplicaço é {result}")
                    continue
                case "4":
                    print(f"o resultado da divisão é {result}")
                    continue
                case _:
                    print(f"opção inválida.")
                    continue

        else:
            print("programa encerrado. ")
            break
    except:
        print(" valores invalidos. ")
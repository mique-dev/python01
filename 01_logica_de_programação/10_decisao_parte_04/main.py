# declração de variaveis
x = float(input("informe o 1º de x: ").strip().replace(",","."))
y = float(input("informe o 2º de y: ").strip().replace(",","."))

# menu
print("1 - soma")
print("2 - subtracao")
print("3 - multiplicacao")
print("4 - divisao")
operador = input(input("informe a opcao desejada: ").strip())

# decisao
match operador:
    case "1":
        print(f"a soma é {x + y}")
    case "2":
        print(f"a subtracao é {x - y}")
    case "3":
        print(f"a multiplicação é {x * y}")
    case "4":
        print(f"a divisao é {x / y}")
    case _:
        print("operação invalida.")
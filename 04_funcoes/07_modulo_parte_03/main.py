# bibliotecas
from modulo import limpar, primeiro_grau, segundo_grau

def main():
    limpar()
    while True:
        print("0 - Sair do programa")
        print("1 - Calcular equacão do 1º grau")
        print("2 - Calcular equação do 2º grau")
        opcao = input("Opção desejada").strip()
        match opcao:
            case "0":
                limpar()
                print("programa encerrado.")
                break
            case "1":
                a = float(input("Informe o coeficiente 'a':").strip().replace(",","."))
                b = float(input("Informe o coeficiente 'b':").strip().replace(",","."))
                limpar()
                x = primeiro_grau(a, b)
                print(f"x = {x}")
                continue
            case "2":
                a = float(input("Informe o coeficiente 'a':").strip().replace(",","."))
                b = float(input("Informe o coeficiente 'b':").strip().replace(",","."))
                c = float(input("Informe o coeficiente 'c':").strip().replace(",","."))
                limpar()
                resultados = segundo_grau(a, b, c)
                for x in resultados:
                    print(f"x = {x}")
                continue
            case _:
                limpar()
                print("Opção ínvalida")
                continue

if __name__ == "__main__":
    main()
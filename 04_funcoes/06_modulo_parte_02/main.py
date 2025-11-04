# função principal
def main():
    # entrada de dados
    nome = input("Infome seu nome:").strip().title()
    idade = int(input("Informe sua idade:").strip())

    # operador termário
    resultado = "é maior de idade" if idade >= 18 else "é menor de idade"

    # saída de dados
    print(f"Nome: {nome} {resultado}")

# protege algoritimo principal
if __name__ == "__main__":
    main()
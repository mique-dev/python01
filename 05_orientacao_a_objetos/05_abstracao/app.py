import os

from classes import Parque

def limpar():
    os.system("cls" if os .name == "nt" else "clear")

def main():
    ingresso = Parque(nome="", idade=0, peso=0)

    ingresso.nome = input("informe o nome: ").strip().title()
    ingresso.idade = int(input("informe a idade: ").strip().title())
    ingresso.peso = float(input("informe o peso: ").strip().replace(",","."))

    limpar()

    while True:
        print("1 - Entrada infantil")
        print("2 - Entrada juvenil")
        print("3 - Entrada adulto")
        print("4 - Sair do programa")
        opcao = input("Informe a opção desejada: ")
        limpar()
        match opcao:
            case "1":
                print(ingresso.entrada_infantil())
                continue
            case "2":
                print(ingresso.entrada_juvenil())
                continue
            case "3":
                print(ingresso.entrada_adulto())
                continue
            case "4":
                print("Progarma finalizado")
                break
            case _:
                print("Opção inválida")

    
if __name__=="__main__":
    main()
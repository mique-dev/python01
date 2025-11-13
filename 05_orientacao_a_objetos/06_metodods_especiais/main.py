import os
from classes import Pessoa

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

limpar()

def main():
    pessoa = Pessoa(nome="", idade=0, genero="", telefone="")

    pessoa.nome = input("Informe o nome: ").strip().title()
    pessoa.idade = int(input("Informe o idade: ").strip().title())
    pessoa.genero = input("Informe o genero: ").strip().title()
    pessoa.telefone = input("Informe o telefone: ").strip().title()

    # saída de dados
    print(pessoa)

if __name__=="__main__":
    main()
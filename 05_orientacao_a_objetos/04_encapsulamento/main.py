from classes import Pessoa

def main():
    usuario = Pessoa(nome="", cpf="")

    usuario.nome = input("informe o nome: ").strip().title()
    usuario.cpf = input("informe o CPF: ").strip()

    print(f"nome: {usuario.nome}")
    print(f"cpf: {usuario.cpf}")

if __name__ == "__main__":
    main()
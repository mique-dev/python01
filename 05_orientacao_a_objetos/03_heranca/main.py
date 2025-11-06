# biblioteca
import os

# nossa biblioteca
from classes import PessoaFisica, PessoaJuridica

# funcao limpar tela
def limpar():
    os.system("cls" if os .name == "nt" else "clear")

# funcaao principal
def main():
    usuario = PessoaFisica(nome="",cpf="", idade=0, email="", telefone="")
    empresa = PessoaJuridica(nome="", cnpj="", email="", telefone="")
    
    limpar()

    while True:
        print("1 - Inserir dados do usuario")
        print("2 - Inserir dados da empresa")
        print("4 - exibir dados do usuario")
        print("5 - exibir dados da empresa")
        print("6 - Sair do programa")
        match opcao:
            case 1:
                usuario.nome = input("informe o nome: ").strip().title()                            
                usuario.cpf = input("informe o nome: ").strip().title()                
                usuario.idade = int(input("informe o nome: ").strip().title())                          
                usuario.email = input("informe o nome: ").strip().title()                
                usuario.telefone = input("informe o nome: ").strip().title()                
                limpar()
                continue
            case 2:
                empresa.nome_fantasia = input("informe o nome da empresa: ").strip().title()
                empresa.cnpj = input("informe o cnpj: ").strip().title()
                empresa.email = input("informe o email: ").strip().title()  
                empresa.telefone = input("informe o telefone: ").strip().title()
                limpar()
                continue
            case 3:
                pass
            case 4:
                usuario.exibir_dados()
            case 5:
                print("Programa encerrado")
                break
            case _:
                print("Opção invalida")
                continue

if __name__ == "__main__":
    main()
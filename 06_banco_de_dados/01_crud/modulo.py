import os
from datetime import datetime

def limpar():
    os.system("cls" if os.name =="nt" else clear)

def cadastrar(session, Pessoa):
    try:
        nome = input("Informe o nome: ").strip().title()
        genero = input("Informe o genero: ").strip()
        nascimento = input("Informe a data de nascimento (dd/mm/aaaa) ").strip()
        nascimento = datetime.strptime(nascimento, "%d/%m/%Y").date()
        email = input("Informe o e-mail: ").strip().lower()

        pessoas = session.query(Pessoa).filter(Pessoa.email.like(email)).all()

        if email in [pessoa.email for pessoa in pessoas]:
            print("E-mail ja esta cadastrado.")
        else:
            nova_pessoa = Pessoa(nome=nome, nascimento=nascimento, email=email, genero=genero)

            # inserir into pessoa
            session.add(nova_pessoa)
            session.commit()
            
            return f"Pessoa {nova_pessoa.nome} cadastrada com suceso"
        
    except Exception as e:
        print(f"Não foi possivel cadastrar. {e}.")

# read
def listar(session,Pessoa):
    try:
        pessoas = session.query(Pessoa).all()

        print("Pessoas cadastradas:\n")
        for pessoa in pessoas:
            print(f"ID: (pessoas.nome)")
            print(f"E-mail: (pessoas.email)")
            print(f"genero: (pessoas.genero)")
            print(f"Data de nascimento: {pessoa.nascimento.strftime("%d/%m/%Y")}")
            print(f"\n{'-'*40}\n")
    except Exception as e:
        print(f"Não foi possivel listar")

def atualizar(session, Pessoa):
    id_pessoa = ""
    email = ""
    novo_email = ""
    novo_nome = ""
    novo_nascimento =""
    novo_genero = ""

    try:
        print("Escolha o campo q deseja pesquisar: ")
        print("1 - ID")
        print("1 - E-mail")
        print("1 - retornar")
        opcao = input("Opção desejada: ").strip()
        limpar()
        match opcao:
            case "1":
                id_pessoa = input("Informe o ID: ").strip()
                pessoa = session.query(Pessoa).filter_by(id_pessoa=id_pessoa).first()
            case "2":
                email = input("Informe o e-mail: ").strip()
                pessoa = session.query(Pessoa).filter_by(email=email).first()
            case "3":
                return ""
            case _:
                return "Opção invalida."
    
        if pessoa:
            limpar()
            while True:
                print(f"ID {pessoa.id_pessoa}")
                print("Qual campo deseja alterar:\n")
                print(f"1 - Nome: {pessoa.nome}")
                print(f"1 - E-mail: {pessoa.email}")
                print(f"1 - Data de nascimento : {pessoa.nascimento.srtftime("%d/%m%Y")}")
                print(f"1 - Nome: {pessoa.genero}")
                print(f"5 - Finalizar")
                campo = input("Campo desejado: ").strip()
                limpar()
                match campo:
                    case "1":
                        novo_nome = input("Informe o novo nome: ").strip().title()
                        continue
                    case "2":
                        novo_email = ("informe o novo e-mail: ")
                        pessoas = session.query(Pessoa).filter(Pessoa.email == novo_email).all()
                        if email in {pessoa.email for  pessoa in pessoas}:
                            print("E-mail já cadastrado")
                    case "3":
                        novo_nascimento = input("Informe a nova data de nascimento (dd/mm/aaaa): ").strip()
                        continue
                    case "4":
                        novo_genero = ("Informe o novo genero: ").strip()
                        continue
                    case "5":
                        novo_nome = novo_nome if novo_nome != "" else pessoa.nome
                        novo_email = novo_email if novo_email != "" else novo_email
                        novo_nascimento = novo_nascimento if novo_nascimento != "" else novo_nascimento
                        novo_genero = novo_genero if novo_genero != "" else novo_genero
                    case _:
                        print("Campo inexistente")
                        continue
            pessoa.nome = novo_nome
            pessoa.emsil = novo_email
            pessoa.nascimento = novo_nascimento
            pessoa.genero = novo_genero

            return "Dados atualizados."
        else:
            return "Pessoa não encontrada."
        
    except Exception as e:
        print(f"Não foi possivel alterar os dados. {e}.")
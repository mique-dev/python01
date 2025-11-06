# classe
class Pessoa:
    #construtoe
    def __init__(self, nome, cpf, email, idade):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.idade = idade

    def exibir_dados(self):
        print(f"nome: {self.nome}")
        print(f"cpf: {self.cpf}")
        print(f"email: {self.email}")
        print(f"idade: {self.idade}")
       
     
# algoritomo principal
if __name__ == "__main__":
    # istancia a classe
    usuario = Pessoa(nome="", cpf="", email="", idade=0)

    # entrada de dados
    usuario.nome = input("informe o nome: ").strip().title()
    usuario.cpf = input("informe o cpf: ").strip()
    usuario.email = input("informe o email: ").strip().title()
    usuario.idade = input("informe o idade: ").strip().title()

    # Saida de dados
    usuario.exibir_dados()
# biblioteca
import os

# classe
class Pessoa:
    # atributos
    nome = "Miqueias Costa"
    idade = 20
    email = "miaqueias.gt867@gmail.com"

    # metodo
    def exibir_dados(self):
        print(f" Nome: {self.nome}")
        print(f" Idade: {self.idade}")
        print(f" E-mail: {self.email}")

if __name__ == "__main__":
    # imstançia a classe (cria nome objeto)
    usuario = Pessoa()

    os.system("cls" if os.name == "nt" else "clear")
              
    # acessando os metodos
    usuario.exibir_dados()
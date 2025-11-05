# bibliotecas
import os

os.system("cls")

# entrada de dados   

nome = input("informe seu nome: ").strip().title()
email =input("informe seu email: ").strip().lower()
CPF =input("informe seu CPF: ").strip()
telefone =input("informe seu telefone: ").strip()
genero =input("informe seu genero: ").strip().title


dicionario = {"nome":nome, "email":email, "CPF":CPF, "telefone":telefone, "genero":genero}

print ("dados do usuario")
for chave in dicionario:
    print(f"{chave}: {dicionario[chave]}")
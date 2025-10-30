# bibliotecas
import os

os.system("cls")

# entrada de dados   
try:
    nome = input("informe seu nome: ").strip().title()
    email =input("informe seu email: ").strip().lower()
    CPF =input("informe seu CPF: ").strip()
    telefone =input("informe seu telefone: ").strip()
    genero =input("informe seu genero: ").strip().title()
    
    dicioario = {"nome":{nome}, "email":{email}, "CPF":{CPF}, "telefone":{telefone}, "genero":{genero}}
except:
    print("infelizmente o programa encerrou devido a um erro")
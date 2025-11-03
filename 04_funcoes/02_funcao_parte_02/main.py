#biblioteca
import os

#fun
def boas_vindas(nome):
    os.system("cls")
    print(f" Seja bem vindo, {nome}!😎")

# algoritio principal
os.system("cls")
nome = input("Infome seu nome:").strip().title()
boas_vindas(nome)
# biblioteca
import os

# funcao

def boas_vindas(nome):
    os.system("cls")
    return f"Seja bem vindo, {nome}!😎"

# oalgoritimo principal
os.system("cls")
nome = input("Infome seu nome:").strip().title()
print(boas_vindas(nome))
resultado = boas_vindas(nome)
print(resultado)
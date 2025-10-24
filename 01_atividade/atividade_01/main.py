# declaração de variaveis

nome = input("informe seu nome: ").strip().title()
email = input("informe seu emai:").strip().lower()
cpf = (input("Informe seu cpf: ").strip())
telefone = (input("Informe seu telefone")).strip()

# inportacao de bibliotecas
import os
import time

while True:
    # limpeza de console
    os.system("cls")

    # mensagems
    print("caregando...")
    time.sleep(5)
    
    break

# saida de dados
print(f"nome: {nome}")
print(f"email: {email}")
print(f"cpf: {cpf}")
print(f"telefone: {telefone}")

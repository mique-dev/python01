# tratamento de execao

# importacao de bibliotecas
import time
import os

# loop de repetcao
try:
    #entrada de dados 
    numero = int(input("informe um número inteiro: ").strip())
    
    # laço de repetição
    while numero >= 0:
        os.system("cls")
        print(numero)
        numero -= 1
        time.sleep(1)
    print("seu aparelho não comsege rodar este programa.")
except:
    print("deu ruin")
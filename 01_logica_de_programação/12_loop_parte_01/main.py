# tratamento de execao
try:
    #entrada de dados 
    numero = int(input("informe um número inteiro: ").strip())
    
    # laço de repetição
    while numero >= 0:
        print(numero)
        numero -= 1

except:
    print("coloque um número inteiro seu animal. ")
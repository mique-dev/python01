# tratamento de excecao
try:
    # entrada de dados
    nome = input("informe seu nome: ").strip().title()
    idade = int(input("informe sua idade: ").strip())
    altura = float(input("informe sua altura: ").strip().replace(",","."))

    # saída de dados
    print(f"nome: {nome}")
    print(f"idade: {idade}")
    print(f"altura: {altura}")
except:
    print("infelizmente o programa encerrou devido a um erro")
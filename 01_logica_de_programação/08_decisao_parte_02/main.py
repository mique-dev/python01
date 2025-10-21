# declaraçao de variaveis
nome = input ("informe seu nome:" ).strip().title()
idade = int (input("informe sua idade: ").strip())
altura = float (input("informe a altura: ").strip())

# estrutura de decisao
if idade >= 12 and altura >= 1.15:
    print (f"entrada de {nome} autorizada.")
else:
    print (f"entrada de {nome} nao autorizada.")
# biblioteca
import os
import math

# limpa console
def limpar():
    os.system("cls")

# funcao de calculo
def quadrado (l):
    return l ** 2

def retangulo (b , h):
    return b * h

def triangulo (b , h):
    return (b * h)/2

#funçaõ para calcular a ipotenusa
def hipotenusa(a , b):
    return math.sqrt((a**2) + (b**2))

# algoritimo principal
limpar()

while True:
    print("1 - Calcular Quadrado")
    print("2 - Calcular Retangulo")
    print("3 - Calcular Triangulo")
    print("4 - calcular a ipotenusa")
    print("5 - Sair do programa")
    opcao = input("Escolha uma opcao:").strip()
    limpar()
    match opcao:
        case "1":
            l = float(input(f"Informe o lado do aquadrado:").strip().replace(",","."))
            resultado = quadrado(l)
            limpar()
            print(f"Área do quadrado: {resultado}")
        case "2":
            b = float(input(f"Informe a base do retangulo:").strip().replace(",","."))
            h = float(input(f"Informe a altura do retangulo:").strip().replace(",","."))
            resultado = retangulo(b , h)
            limpar()
            print(f"área do retangulo: {resultado}")
            continue
        case "3":
            b = float(input(f"Informe a base do triangulo:").strip().replace(",","."))
            h = float(input(f"Informe a altura do triangulo:").strip().replace(",","."))
            resultado = retangulo(b , h)
            limpar()
            print(f"área do retangulo: {resultado}")
            continue
        case "4":
            a = float(input(f"Informe o primeiro cateto:").strip().replace(",","."))
            b = float(input(f"Informe o segundo cateto:").strip().replace(",","."))
            resultado = hipotenusa(a , b)
            limpar()
            print(f"A ipotenusea é: {resultado}")
        case "5":
            print("programa emcerrado.")
            break
        case _:
            print("oOpção invalida.")


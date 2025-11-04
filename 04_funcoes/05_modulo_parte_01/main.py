# importa as funcooes
import modulo as m

m.limpar()

while True:
    print("1 calcular quadrdado")
    print("2 calcular Retangulo")
    print("3 calcular Triangulo")
    print("4 calcular Circulo")
    print("5 Clacular Trpezio")
    print("6 Sair do programa")
    opcao = input("Opção deseja:").strip()
    m.limpar()
    match opcao:
        case "1":
            l = float(input(f"Informe o lado do aquadrado:").strip().replace(",","."))
            m.limpar()
            area = m.quadrado(l)
            print(f"Área do quadrado: {area}")
            continue
        case "2":
            b = float(input(f"Informe o a base do retangulo:").strip().replace(",","."))
            h = float(input(f"Informe a altura do retangulo:").strip().replace(",","."))
            m.limpar()
            area = m.retangulo(b, h)
            print(f"Área do quadrado: {area}")
            continue
        case "3":
            b = float(input(f"Informe o a base do triangulo:").strip().replace(",","."))
            h = float(input(f"Informe a altura do triangulo:").strip().replace(",","."))
            m.limpar()
            area = m.triangulo(b, h)
            print(f"Área do triangulo: {area}")
            continue
        case "4":
            r = float(input(f"Informe o raio do circulo: ").strip().replace(",","."))
            m.limpar()
            raio = m.circulo(r)
            print(f"Área do circulo: {raio}")
            continue
        case "5":
            b = float(input(f"Informe a base do trapezio:").strip().replace(",","."))
            B = float(input(f" Informe a base maior do trapezio:").strip().replace(",","."))
            h = float(input(f"Informe a altura do trapezio:").strip().replace(",","."))
            m.limpar()
            area = m.trapezio(b, B, h)
            print(f" Área do trapezio: {area}")
            continue
        case "6":
            break
        case _:
            print(" É só digitar uma das opções seu animal!!! 🤬")

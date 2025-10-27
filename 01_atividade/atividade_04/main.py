# TODO: atividade
"""
Crie um programa que recebe do usuário o nome e a idade, e em seguida, exiba na tela uma lista de filmes, suas respectivas salas e classificações indicativas:
C
O usuário deverá escolher o filme, e caso ele tiver a idade mínima para ver o filme, imprime o ingresso e encerra o programa. Caso o usuário não tenha a idade mínima, o programa impede a entrada do usuário e re-exibe a lista de filmes para que o mesmo escolha outro filme.
"""
try:
    nome = input("Informe seu nome: ").strip().title()
    idade = int(input("Informe sua idade: ").strip())

    # lista de filmes
    sala_1 = " a roda quadrada"
    sala_2 = " a volta dos que não foram"
    sala_3 = " poeira em alto mar"
    sala_4 = " o q importa é só o importante"
    sala_5 = " oq está cheio não está vazio"

    # loop
    while True:
        # menu filmes
        print(f"sala 1 - {sala_1} -livre")
        print(f"sala 2 - {sala_2} - 12 anos")
        print(f"sala 3 - {sala_3} - 14 anos")
        print(f"sala 4- {sala_4} - 16 anos")
        print(f"sala 5 - {sala_5} - 18 anos")
        sala = input(" Informe a sala que dessejada: ").strip().lower()

        # verificação da sala
        match sala:
            case "1":
                filme = sala_1
                idade_minima = 0
                pass
            case "2":
                filme = sala_2
                idade_minima = 12
                pass
            case "3":
                filme = sala_3
                idade_minima = 14
                pass
            case "4":
                filme = sala_4
                idade_minima = 16
                pass
            case "5":
                filme = sala_5
                idade_minima = 18
                pass
            case _: 
                print("esta sala n existe")
        if idade >= idade_minima:
            print(f"{nome} escolheu {filme} e pode assistir ao filme. ")
            break
        else:
            print(f"{nome} não foi autorizado a ver {filme}.")
            continue
except Exception as e:
    print(f"lamento mais fui de F.{e}")

 
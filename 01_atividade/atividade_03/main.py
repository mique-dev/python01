# TODO: atividade 

# tratamento de exceção

try:
    # entrada de dados
    
    nome = input("Informe seu nome: ").strip().title()
    peso = float(input("Informe seu peso: ").strip().replace(",","."))
    altura = float(input("Informe sua altura em metros: ").strip().replace(",","."))
    
    # calcule do IMC

    IMC = peso / (altura ** 2)

    # exibe o imc do usuario
    print (f"{nome}, seu IMC é: {IMC:.2f}")

    # diagnóstico do IMC
    if IMC < 18.0:
       print(f"{nome} esta muuuito magro. ")      
    if IMC < 25:
       print(f"{nome} Voçê esta com o peso ideal. ")
    if IMC < 30:
       print(f"{nome} Voçê esta com sobrepeso. ")
    elif IMC < 35:
       print(f"{nome} esta com obesidade grau 1. ")
    elif IMC < 40:
       print(f"{nome} esta com obesidade grau 2. ")
    else:
       print(f"Por favor. Não pule de um lugares muito altos. vai quebrar o planeta. ")

except Exception as e:
    print(f"Por favor, insira valores válidos.{e}")


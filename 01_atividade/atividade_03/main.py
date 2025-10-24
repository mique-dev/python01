# entrada de dados
nome = input("Informe seu nome").strip().title()
peso = input(float("Informe seu peso")).strip()
altura = input(float("Informe sua altura")).strp()
IMC = round(peso/altura**2,2)
ptint = ("Informe {IMC}")

if IMC <= 18.0:
    print("Voçê esta muuuito magro. ")
elif IMC <= 25.0:
    print("Voçê esta com um peso bacana. ")
elif IMC <= 35.0:
    print("Voçê esta com um peso noemal. ")
elif IMC <= 40.9:
    print("Acho q voçê ganhou um pouquinho de peso. ")
else:
    print("Por favor. Não pule de um lugares muito altos. vai quebrar o planeta. ")
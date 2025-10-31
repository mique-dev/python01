# declaracao de dicionario

usuarios = [
    {
        'nome': "Fulano", 
        'idade': 20, 
        'email': "fulano@gmail.com"
    },
    {
        'nome': "Beltrano", 
        'idade': 30,
        'email': "beltrano@gmai.com"
    },
    {
        'nome': "Beltrano", 
        'idade': 30,
        'email': "beltrano@cgmail.com"
    }
]

# exibe os dados dos usuarios
for usuario in usuarios:
    print(f"\n{'-'*40}\n")
    for chave in usuario:
        print(f"{chave}captalize(): {usuario[chave]}")

class Banco:

    def __init__(self, nome, saldo, cpf, agencia, conta):
        self.nome = nome
        self.saldo = saldo
        self.cpf = cpf
        self.agencia = agencia
        self.conta = conta
        
    def exibir_dados():
        print("Nome: {self.nome}")
        print("Saldo: {self.saldo}")
        print("Cpf: {self.cpf}")
        print("numero da agencia: {self.agencia}")
        print("numero da conta: {self.conta}")
        

        def
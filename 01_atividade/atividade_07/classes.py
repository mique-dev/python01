import os

class Conta:
    def __init__(self, titular, cpf, n_agencia, n_conta, saldo):
        self.nome = titular
        self.cpf = cpf
        self.saldo = saldo
        self.agencia = n_agencia
        self.conta = n_conta
    
    def consultar_dados(self):
        print(f"Nome do titular da conts: {self.nome}")
        print(f"CPF do titular: {self.cpf}")
        print(f"Agencia da conta: {self.agencia}")
        print(f"Numero da onta: {self.conta}")
        print(f"Saldo da conta: R${self.saldo}")
    
    def depositar(self, valor):
        self.saldo += valor
        print(f"Deposito realizado com sucesso. Seu saldo atual é de R${self.saldo}")
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return self.saldo
        else:
            print("Saldo insuficiente")
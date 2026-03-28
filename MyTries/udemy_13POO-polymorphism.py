#!/usr/bin/python3

class ContaBancaria:
    def __init__(self, numeroConta, agencia, dataAbertura):
        self.numeroConta = numeroConta
        self.agencia = agencia
        self.dataAbertura = dataAbertura
        self._saldo = 0 # Atributo protegido (Encapsulado)
        self.beneficios = []

    def __iter__(self):
        pass

    def __str__(self):
        tipo = self.__class__.__name__ # nome da classe do objeto instanciado
        return f"Conta: {self.numeroConta} | Tipo: {tipo} | Saldo: R${self._saldo}"
    
    def consultar_saldo(self): # o "Getter": para ver saldo sem 'tocar' saldo
        return self._saldo

    def deposito(self, valor):
        if valor <= 0:
            return f'Erro! Valor inválido!'
        self._saldo += valor
        return f'Depósito de R${valor} realizado!'
    
    # método transferência fica nesta classe Pai (Base) para que todas as classes 
    # Filhas o herdem, evitando repetição de código (DRY - Don't repeat yourself) 
    # em métodos como transferenciaCorrente e transferenciaPoupanca para cada uma.
    # Ele demonstra como a classe Base pode definir fluxo lógico que as filhas executam.
    def transferencia(self, conta_destino, valor):
        resultado_saque = self.saque(valor)
        
        if resultado_saque.startswith('Erro'):
            return f'Transferência falhou: {resultado_saque}'
        conta_destino.deposito(valor)
        return f'Transferência de R${valor} para a conta {conta_destino.numeroConta} realizada!'

class ContaCorrente(ContaBancaria):
    def saque(self, valor):
        limite = 1000 if 'saldo negat até R$1000' in self.beneficios \
                      else 0
        if valor > (self._saldo + limite):
            return 'Erro! Saldo insuficiente!'
        self._saldo -= valor
        return f'Saque de R${valor} realizado na Conta Corrente.'
    
    def pagar_taxa(self):
        return self.saque(10)

class ContaPoupanca(ContaBancaria):
    def saque(self, valor): # sem limite especial
        if valor > (self._saldo):
            return 'Erro! Saldo insuficiente!'
        self._saldo -= valor
        return f'Saque de R${valor} realizado na Conta Poupança.'

    def pagar_taxa(self):
        return "Isento de taxa"


if __name__ == '__main__':
    # print("Novas contas...")
    conta_joao = ContaCorrente(101, '001', '01/01/2024')
    conta_maria = ContaPoupanca(202, '001', '01/01/2026')
    conta_marcelo = ContaCorrente(132, '001', '27/03/2026')
    contas_do_dia = [conta_joao, conta_maria, conta_marcelo]
    print(conta_joao)
    print(conta_maria)
    print(f'{conta_marcelo}\n')
    
    # Operações
    conta_joao.deposito(500)
    print("Depósito na conta 101 (do João)...")
    print(conta_joao)
    print(conta_maria)
    print(f'{conta_marcelo}\n')
    
    print("Transferência do João para a Maria (conta 202)...")
    print(conta_joao.transferencia(conta_maria, 200))
    print(conta_joao)
    print(conta_maria)
    print(f'{conta_marcelo}\n')

    print("Transferência da Maria para o Marcelo (conta 132)...")
    print(conta_maria.transferencia(conta_marcelo, 150))
    print(conta_joao)
    print(conta_maria)
    print(f'{conta_marcelo}\n')

    print("Cobrança de taxa de manutenção das contas...")
    for conta in contas_do_dia:
        # if conta.__class__.__name__ != "ContaPoupanca": 
        conta.pagar_taxa()
    print(conta_joao)
    print(conta_maria)
    print(f'{conta_marcelo}\n')

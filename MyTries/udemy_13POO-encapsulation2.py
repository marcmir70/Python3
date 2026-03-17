#!/usr/bin/python3

class ContaBancaria:
    def __init__(self, numeroConta,  tipoConta, agencia, dataAbertura):
        self.numeroConta = numeroConta
        self.tipoConta = tipoConta
        self.agencia = agencia
        self.dataAbertura = dataAbertura
        self._saldo = 0 # Atributo protegido (Encapsulado)
        self.beneficios = []

    def __iter__(self):
        pass

    def __str__(self):
        return f"Conta: {self.numeroConta} | Tipo: {self.tipoConta} | Saldo: R${self._saldo}"
    
    def consultar_saldo(self): # o "Getter": janela para ver saldo sem tocá-lo
        return self._saldo

    def deposito(self, valor):
        if valor <= 0:
            return f'Erro! Valor de depósito ({valor}) inválido!'
        self._saldo += valor
        return f'Depósito de R${valor} realizado com sucesso!'

    def saque(self, valor):
        limite = 1000 if 'saldo negat até R$1000' in self.beneficios \
                      else 0
        if valor > (self._saldo + limite):
            return 'Erro! Saldo insuficiente!'
        self._saldo -= valor
        return f'Saque de R${valor} realizado.'

    def transferencia(self, conta_destino, valor):
        resultado_saque = self.saque(valor)
        
        if resultado_saque.startswith('Erro'):
            return f'Transferência falhou: {resultado_saque}'
        conta_destino.deposito(valor)
        return f'Transferência de R${valor} para a conta {conta_destino.numeroConta} realizada!'

if __name__ == '__main__':
    conta_joao = ContaBancaria(101, 'Corrente', '001', '01/01/2024')

    # 1. Forma correta de ver o saldo
    print(f"Saldo inicial: R${conta_joao.consultar_saldo()}")
    
    # 2. Tentativa de alteração direta - Python permite, mas programador não deve!
    conta_joao._saldo = 1000000 
    print(f"Saldo após 'invasão': R${conta_joao.consultar_saldo()}")
    
    # 3. O uso correto via interface
    conta_joao.deposito(500)
    print(f"Saldo final oficial: R${conta_joao.consultar_saldo()}")
    
    # conta_maria = ContaBancaria(202, 'Poupanca', '001', '01/01/2026')
    # print("Novas contas...")
    # print(conta_joao)
    # print(f'{conta_maria}\n')
    
    # # Operações
    # conta_joao.deposito(500)
    # print("Depósito na conta 101 (do João)...")
    # print(conta_joao)
    # print(f'{conta_maria}\n')
    
    # print("Transferência do João para a Maria (conta 202)...")
    # print(conta_joao.transferencia(conta_maria, 200))
    # print(conta_joao)
    # print(f'{conta_maria}\n')

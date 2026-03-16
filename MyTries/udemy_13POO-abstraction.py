#!/usr/bin/python3
# Abstração: quando se decide que ContaBancaria tem numeroConta, saldo, deposito; 
#     ignorando cor do cartão e endereço da agência física, focando no essencial
# Exemplo: em sistema de RH, um "Funcionário" precisa de nome e salário. 
#     Não importa a cor dos olhos ou a altura dele.
# Exercício: modelar classe ContaBancaria. 
#     Quais seriam os dados essenciais (atributos) e as ações (métodos) mínimas?

class ContaBancaria:
    def __init__(self, numeroConta,  tipoConta, agencia, dataAbertura):
        self.numeroConta = numeroConta
        self.tipoConta = tipoConta
        self.agencia = agencia
        self.dataAbertura = dataAbertura
        self.saldo = 0
        self.beneficios = []

    def __iter__(self):
        pass

    def __str__(self):
        return f"Conta: {self.numeroConta} | Tipo: {self.tipoConta} | Saldo: R${self.saldo}"

    def deposito(self, valor):
        if valor <= 0:
            return f'Erro! Valor de depósito ({valor}) inválido!'
        self.saldo += valor
        return f'Depósito de R${valor} realizado com sucesso!'

    def saque(self, valor):
        limite = 1000 if 'saldo negat até R$1000' in self.beneficios \
                      else 0
        if valor > (self.saldo + limite):
            return 'Erro! Saldo insuficiente!'
        self.saldo -= valor
        return f'Saque de R${valor} realizado.'

    # def transferencia(self, valor, cpfDest, bancoDest, agenDest, numCtaDest):
    def transferencia(self, conta_destino, valor):
        # Abstraímos a transferência como: "Tiro de mim e coloco no outro"
        #    Não importam detalhes da conta_destino, 
        #    só que ela seja um objeto que aceita depósitos.
        resultado_saque = self.saque(valor)
        
        if resultado_saque.startswith('Erro'):
            return f'Transferência falhou: {resultado_saque}'
        # O objeto atual (self) usa o método do objeto destino
        conta_destino.deposito(valor)
        return f'Transferência de R${valor} para a conta {conta_destino.numeroConta} realizada!'

if __name__ == '__main__':
    # Criando (Instanciando) os objetos
    conta_joao = ContaBancaria(101, 'Corrente', '001', '01/01/2024')
    conta_maria = ContaBancaria(202, 'Poupanca', '001', '01/01/2026')
    print("Novas contas...")
    print(conta_joao)
    print(f'{conta_maria}\n')
    
    # Operações
    conta_joao.deposito(500)
    print("Depósito na conta 101 (do João)...")
    print(conta_joao)
    print(f'{conta_maria}\n')
    
    print("Transferência do João para a Maria (conta 202)...")
    print(conta_joao.transferencia(conta_maria, 200))
    print(conta_joao)
    print(f'{conta_maria}\n')

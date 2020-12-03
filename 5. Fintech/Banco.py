from random import uniform, randint


class Cliente:
    def __init__(self, nome, renda):
        self.nome = nome
        self.renda = renda


class Conta:
    def __init__(self, cliente):
        self.numero_conta = randint(0, 10000)
        self.agencia = 1001
        self.saldo = 0
        self.cliente = cliente
        self.credito = 0

    def consultar_saldo(self):
        print(f"\nSeu saldo atual é : R$ {self.saldo:.2f}")
        print(f"Seu crédito especial atual é : R$ {self.credito:.2f}")
        print(f"Saldo total: R$ {(self.saldo+self.credito):.2f}")

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

    def credito_especial(self, renda):
        self.credito = uniform(0, renda)
        print(f"\nSeu crédito especial é de R$ {self.credito:.2f}, totalizando um saldo de R$ {(self.saldo+self.credito):.2f}")


nome_cliente = input("Digite seu nome: ")
renda_cliente = float(input("Informe sua renda mensal: "))

c1 = Cliente(nome_cliente, renda_cliente)

conta_c1 = Conta(c1)

print(f"\nNúmero da conta: {conta_c1.numero_conta}")
print(f"Agência: {conta_c1.agencia}")
print(f"Cliente: {conta_c1.cliente.nome}")
print(f"Renda mensal: {conta_c1.cliente.renda}")
print(f"Saldo atual: {conta_c1.saldo}")

resposta = -1
while resposta != 0:

    resposta = int(input('''\nO que deseja fazer?: \n\n\t1. Saque\n\t2. Depósito\n\t3. Consultar saldo
    4. Solicitar crédito especial\n\t0. Sair\n'''))

    if resposta == 1:
        saque = float(input("\nValor a sacar: "))
        conta_c1.sacar(saque)

    elif resposta == 2:
        deposito = float(input("\nValor a depositar: "))
        conta_c1.depositar(deposito)

    elif resposta == 3:
        conta_c1.consultar_saldo()

    elif resposta == 4:
        resposta2 = int(input("\nGostaria de obter o crédito especial? \n\n1. SIM \n2. NÃO\n"))

        if resposta2 == 1:
            conta_c1.credito_especial(c1.renda)
        else:
            pass

    elif resposta == 0:
        pass

    else:
        print("Entrada inválida!")
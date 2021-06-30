#Crie uma classe chamada Conta para simular as operações de uma conta corrente. 
# Sua classe deverá ter os atributos Titular e Saldo, e os métodos Sacar e Depositar. 
# Crie um objeto da classe Conta e teste os atributos e métodos implementados.​ 
# Adicione uma regra no método Sacar, onde o usuário só poderá sacar se o Saldo for maior que zero, caso contrário mostre a mensagem na tela: "Você não tem saldo suficiente para essa operação."
class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    def sacar(self, valor):
        if self.saldo < valor:
            print('\nVocê não tem saldo suficiente para essa operação.')
        else:
            self.saldo -= valor
    def depositar(self, valor):
        self.saldo += valor
    def mostrarDados(self):
        return f'''
        Titular: {self.titular}
        Saldo: R$ {self.saldo:.2f}'''


pessoa1 = Conta('Felipe Menezes Silva Sá', 548.71)
print(pessoa1.mostrarDados())

pessoa1.sacar(600)
print(pessoa1.mostrarDados())

pessoa1.sacar(430.93)
print(pessoa1.mostrarDados())

pessoa1.depositar(945.67)
print(pessoa1.mostrarDados())
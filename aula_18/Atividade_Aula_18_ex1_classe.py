#Crie uma classe chamada Conta para simular as operações de uma conta corrente. 
# Sua classe deverá ter os atributos Titular e Saldo, e os métodos Sacar e Depositar. 
# Crie um objeto da classe Conta e teste os atributos e métodos implementados.​ 
# Adicione uma regra no método Sacar, onde o usuário só poderá sacar se o Saldo for maior que zero, 
# caso contrário mostre a mensagem na tela: "Você não tem saldo suficiente para essa operação."
# Fazer o método sacar(), se o saldo for menor ou igual a 0, 
# retorne uma mensagem dizendo que o saldo é insuficiente, caso o contrário, realize a operação de saque e mostre o saldo atual dessa conta;

class Conta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
    
    def __str___(self):
        if(self.saldo) == 0:
            return f'''
        Titular: {self.titular}'''
        else:
            return f'''
            Titular: {self.titular}
            Saldo: R$ {self.saldo:.2f}'''
        
    def depositar(self, deposito):
        self.saldo = self.saldo+deposito
        self.extrato()

    def sacar(self, valor):
        if valor>0:
            print("Você não pode sacar ZERO reais !")
            self.extrato()
            if self.saldo < valor:
                print("Você não tem saldo suficiente para essa operação.")
                self.extrato()
            else:
                self.saldo =self.saldo - valor
                self.extrato()

    def extrato(self):
        print(f"Seu saldo é R${self.saldo:.2f}")

    


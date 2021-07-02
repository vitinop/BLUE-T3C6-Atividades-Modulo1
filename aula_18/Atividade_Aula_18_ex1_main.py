#Crie uma classe chamada Conta para simular as operações de uma conta corrente. 
# Sua classe deverá ter os atributos Titular e Saldo, e os métodos Sacar e Depositar. 
# Crie um objeto da classe Conta e teste os atributos e métodos implementados.​ 
# Adicione uma regra no método Sacar, onde o usuário só poderá sacar se o Saldo for maior que zero, caso contrário mostre a mensagem na tela: "Você não tem saldo suficiente para essa operação."
from Atividade_Aula_18_ex1_classe import Conta
if __name__== '__main__':
    banco = list()

    while True:
        conta=Conta(input("Titular: "))
        banco.append(conta)
        for o in conta:
            banco[o].depositar(float(input("Quanto você deseja depositar? R$")))
            banco[o].sacar(float(input("Quanto você deseja sacar? R$ ?")))
        
        

        resposta = str(input("Gostaria de realizar outra operação? [S/N]: ")).upper().strip()[0]
        if resposta == 'N':
            break

    

    # for o in banco:
    #     print(o)
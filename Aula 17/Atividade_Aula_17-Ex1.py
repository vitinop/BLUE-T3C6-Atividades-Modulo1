# Utilizando os conceitos de Orientação a Objetos ( vistos na aula anterior), 
# crie um lançador de dados e moedas em que o usuário deve escolher o objeto a ser lançado.
# Não esqueça que os lançamentos são feitos de forma randômica
from random import randint

class Lancador:
    def __init__(self):
        self.moeda = randint(0,1)
        self.dadoface = randint(1,6)
    def jogarMoedaFunc(self):
        if self.moeda==1:
            self.resultado="Cara"
        else:
            self.resultado="Coroa"
        return self.resultado        
    def jogarDadoFunc(self):
        return self.dadoface

pergunta=str(input("Gostaria de jogar dados ou a moeda ? :")).lower().strip()[0]
if pergunta=="m":
    jogar_moeda= Lancador()
    print(f"O resultado da moeda é: {jogar_moeda.jogarMoedaFunc()}")
elif pergunta=="d":
    jogar_dado=Lancador()
    print(f"O resultado do dado é: {jogar_dado.jogarDadoFunc()}")
else:
    print("Escolha Inválida")
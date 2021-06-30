import random
sortnumber = random.randint(0,10)
usernumber =int (input ("Insira um numero de 0 a 10 e tente adivinhar o numero escolhido pela maquina: "))
contadorerros= 1
if usernumber == sortnumber:
        print(f"Parabens você é praticamente o oráculo e acertou com {contadorerros} tentativa")
while usernumber != sortnumber:
    usernumber =int(input("Errou feio, errou rude! Tente novamente inserindo um novo valor: "))
    contadorerros= contadorerros + 1
    #print(sortnumber)#

print(f"Parabens você tem os dotes da mãe Diná e acertou após {contadorerros} tentativas")
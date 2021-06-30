#04 (DESAFIO) Crie um jogo onde o computador vai “pensar” em um número entre
#0 e 10. O jogador vai tentar adivinhar qual número foi escolhido até acertar, 
# entre os palpites diga ao jogador se o número do computador é maior ou menor ao que ele digitou,
# no final mostre quantos palpites foram necessários para vencer
import random
sortnumber = random.randint(0,10)
contadorerros= 1
#print(sortnumber)
#########
usernumber=int (input ("Insira um numero de 0 a 10 e tente adivinhar o numero escolhido pela maquina: "))
if usernumber == sortnumber:
        print(f"Parabens você é praticamente o oráculo e acertou com {contadorerros} tentativa")  
elif sortnumber>usernumber:
     print("""Errou feio, errou rude!
        O numero inserido é menor que o numero sorteado""")
     contadorerros= contadorerros + 1
elif sortnumber<usernumber:
    print("""Errou feio, errou rude!
        O numero inserido é maior que o numero sorteado""")
##########
while usernumber != sortnumber:
    usernumber=int (input ("Insira um numero de 0 a 10 e tente adivinhar o numero escolhido pela maquina: "))
    if usernumber == sortnumber:
        print(f"Parabens você tem os dotes da mãe Diná e acertou após {contadorerros} tentativas")
    elif sortnumber>usernumber:
        print("""Errou feio, errou rude!
        O numero inserido é menor que o numero sorteado""")
        contadorerros= contadorerros + 1
    elif sortnumber<usernumber:
        print("""Errou feio, errou rude!
        O numero inserido é maior que o numero sorteado""")
        contadorerros= contadorerros + 1
    
    
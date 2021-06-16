#02 - Crie um programa que pergunte ao usuário um número inteiro e faça a tabuada desse número.
from time import sleep
num=int(input(f"Olá, insira um número inteiro: "))
print (f"A tabuada do numero {num} é :")

for contador in range(0,10) :
    print (f"{num}x{contador+1}={num*contador}")
    sleep (0.5)
    


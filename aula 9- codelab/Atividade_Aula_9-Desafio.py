# Desafio: Faça um programa que ajude um jogador da MEGA SENA a criar
# palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6
# números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
#jogo contem 6 numeros
from random import randint
listaPrincipal=[]
quantJogos=int(input("Gostaria de fazer quantos jogos? : "))
for i in range(quantJogos):
    lista=[]
    while True:
        numero=randint(1,60)
        numero.sort()
        if numero not in lista:
            lista.append(numero)
        if len(lista) == 6:
            break
    listaPrincipal.append(lista)
for i in range(quantJogos):
    print(f"O {i+1}º jogo é: {listaPrincipal[i]}" )
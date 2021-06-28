# Utilizando os conceitos aprendidos até dicionários, crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# O programa tem que:
# • Perguntar quantas rodadas você quer fazer;
# • Guardar os resultados dos dados em um dicionário.
# • Ordenar esse dicionário, sabendo que o vencedor tirou o maior número no dado.
# • Mostrar no final qual jogador ganhou mais rodadas e foi o grande campeão.
# Obs: O projeto deve ser feito individualmente e entregue até o final da aula 16.
import os #Biblioteca para limpar o console
from random import randint #Biblioteca para gerar os números dos dados aleatórios
import operator #Biblioteca para ordenar os dicionarios por ordem de Valor das Chaves
from time import sleep #Biblioteca para definir tempo de sleep entre uma linha e outra
from tqdm import tqdm #Biblioteca para gerar a barra de progresso
from rich import print #Biblioteca para decorar os textos
import pygame
rodada = dict() # Criação de dicionário temporário que receberá as informações de cada rodada
pygame.init()
pygame.mixer.music.load("C:\\Users\\Victor Luz\\Desktop\\Blue\\Repositório Módulo 1\\GitHub\\BLUE-T3C6-Atividades-Modulo1\\Projetos\\Projeto 3 - Jogo de Dados\\Turtles-open.wav")
pygame.mixer.music.play()

print(f"""[green]
       .-------.    ______
      /   o   /|   /\     \ 
     /_______/o|  /o \  o  \ 
     | o     | | /   o\_____\           Bem Vindo a jogo dos Dados !!!!
     |   o   |o/ \o   /o    /
     |     o |/   \ o/  o  /
     '-------'     \/____o/ [/green]
""")
print(f'='*30)
dado= { 
"dado1":"""
 _____     
|     |
|  o  |
|     |
 ----- """,
"dado2":"""
 _____   
|    o|  
|     |  
|o    |
 -----  """,
"dado3":"""
 _____  
| o   |
|  o  |
|   o |    
 ----- """,
"dado4":"""
 _____      
|o   o|
|     |
|o   o|
 ----- """,
"dado5":"""
 _____ 
|o   o|
|  o  |
|o   o|
 ----- """,
"dado6":"""
 _____ 
|o   o|
|o   o|
|o   o|
 -----"""}
while True:
    rodadas = int(input('Quantas rodadas você quer jogar? '))
    sleep(1)
    print(f'='*30)
    vitPlayer1 = vitPlayer2 = vitPlayer3 = vitPlayer4 = 0 # Contadores para os resultados das rodadas
    print('[yellow]ROLANDO OS DADOS...')
    print()
    for i in tqdm(range(100)): # Barra de progresso lib TDQM para decoração do jogo
        sleep(0.001)
    print()
    dadosResult = list() # criação das lista temporária para receber o resultado dos dados
    for r in range(rodadas):
        rodada['player1'] = randint(1, 6) # Randint para gerar números aleatórios dos dados
        rodada['player2'] = randint(1, 6)
        rodada['player3'] = randint(1, 6)
        rodada['player4'] = randint(1, 6)
        sleep(1)
        print(f"{r + 1}º rodada: {rodada}")
        for player in rodada.keys():
            print(f"{player}{dado['dado'+str(rodada[player])]}")
            sleep(1)
        print(f"{r + 1}º rodada: {rodada}") # Visualização das jogadas em tempo real
        sleep(1)
        if (rodada['player3'] < rodada['player1'] > rodada['player2']) and rodada['player1'] > rodada['player4'] : # Inclusão das vitórias dos jogadores
            vitPlayer1+=1
        elif (rodada['player3'] < rodada['player2'] > rodada['player1']) and rodada['player2'] > rodada['player4'] :
            vitPlayer2+=1
        elif (rodada['player2'] < rodada['player3'] > rodada['player1']) and rodada['player3'] > rodada['player4'] :
            vitPlayer3+=1
        elif (rodada['player3'] < rodada['player4'] > rodada['player2']) and rodada['player4'] > rodada['player1'] :
            vitPlayer4+=1
        empates = rodadas - (vitPlayer1+vitPlayer2+vitPlayer3+vitPlayer4)
        sortedResult = sorted(rodada.items(), key=operator.itemgetter(1), reverse=True) # lista ordenada utilizando a lib Operator
        # itemgettetr (1) para ordenar pelo VALOR , REVERSE = True para ordem decrescente (o maior valor ganha)
        dadosResult.append(sortedResult) # Cada dicionário temporário criado é adicionado ao dadosResult que contem todos as rodadas
        os.system('cls' if os.name == 'nt' else 'clear') #Comando para limpar console
        sleep(1)
    (f'='*30)
    if (vitPlayer2 < vitPlayer1 > vitPlayer3) and vitPlayer1 > vitPlayer4: # Estrutura condicional para demonstrar quem ganhou mais rodadas
        print(f"O Campeão é o Jogador 1 com {vitPlayer1} vitórias.")
    elif (vitPlayer3 < vitPlayer2 > vitPlayer1) and vitPlayer2 > vitPlayer4:
        print(f"O Campeão é o Jogador 2 com {vitPlayer2} vitórias.")
    elif (vitPlayer2 < vitPlayer3 > vitPlayer1) and vitPlayer3 > vitPlayer4:
        print(f"O Campeão é o Jogador 3 com {vitPlayer3} vitórias.")
    elif (vitPlayer2 < vitPlayer4 > vitPlayer1) and vitPlayer4 > vitPlayer1:
        print(f"O Campeão é o Jogador 3 com {vitPlayer4} vitórias.")
    else:
        print(f"O jogo Empatou!")
    print("""[yellow]
             .-=========-.
             \ -=======- /
             _|   .=.   |_
            ((|  {{1}}  |))
             \|   /|\   |/
              \__ '`' __/
                _`) (`_
              _/_______\_
             /___________\ 
            [/yellow]""")
    sleep(1)
    print(f'{"[bold yellow]ESTATÍSTICAS DO JOGO[/bold yellow]":^30}')
    print(f'''
    JOGADOR 1 = {vitPlayer1} VITÓRIAS
    JOGADOR 2 = {vitPlayer2} VITÓRIAS
    JOGADOR 3 = {vitPlayer3} VITÓRIAS
    JOGADOR 4 = {vitPlayer4} VITÓRIAS
    EMPATES = {empates}
    ''')
    votacao = str(input("Gostaria jogar novamente? [S/N]: ")).upper().strip()[0]#Comando para limpar console
    os.system('cls' if os.name == 'nt' else 'clear')
    if votacao == 'S':
        contadorvitorias=0
        contadorderrotas=0 
    elif votacao == 'N':
        break
        
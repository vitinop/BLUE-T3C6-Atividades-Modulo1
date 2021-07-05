# Projeto 04 - Simulador de votação:
# Crie um programa que simule um sistema de votação, ele deve receber votos até
# que o usuário diga que não tem mais ninguém para votar, esse programa precisa ter
# duas funções:
# A 1° Função precisa ser chamada autoriza_voto() ela vai receber como parâmetro o
# ano de nascimento de uma pessoa que será digitado pelo usuário, retornando um
# valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e
# OBRIGATÓRIO nas eleições.
# A 2° Função será a votacao(), ela vai receber dois parâmetros, autorização (que virá
# da função autoriza_voto()) e o voto que é o número que a pessoa votou.
# Se ela não puder votar, a 2° função terá que retornar “Você não pode votar”, caso o
# contrário a 2° função deve validar o número que a pessoa escolheu, ela pode
# escolher de 1 a 5 (crie 3 candidatos para a votação):
# ● 1, 2 ou 3 - Votos para os respectivos candidatos
# ● 4- Voto Nulo
# ● 5 - Voto em Branco
# Sua função votacao() tem que calcular e mostrar:
# ● O total de votos para cada candidato;
# ● O total de votos nulos;
# ● O total de votos em branco;
# ● Qual candidato venceu a votaçãojose = joao = antonio = carlos = totaldevotos = votobranco = votonulo =pernulo = perbranco =0
import os                       # Biblioteca para limpar o terminal.
# from os import getcwd           #
from time import sleep          # Biblioteca para adicionar deley as ações. 
# import pygame                   # Biblioteca para adicionar som.
import datetime                 # Biblioteca para importar a data do computador

lista_votos= list([0,0,0,0,0])

continuar_votando=''

def autoriza_voto_func(idade_Pessoa): #Função para verificação de idade para autorizar ou nao o voto do usuário
    if idade_Pessoa<16:
        return 'Voto Negado'
    elif idade_Pessoa>=70:
        return 'Voto Opcional'
    else:
        return 'Voto Obrigatório'


def votacao_Func(voto=0): #Função para atribuição de um voto válido para um dos candidatos
    # pygame.init()
    # pygame.mixer.music.load(getcwd() + 'voto_confirmado.mp3')
    # totaldevotos += 1
    if voto == 1:
        return ["Voto no canditadato José computado com sucesso",0]
    elif voto == 2:
        return ["Voto no canditadato João computado com sucesso",1]
    elif voto == 3:
        return ["Voto no canditadato Antônio computado com sucesso",2]
    elif voto == 4:
        return ["Voto em branco computado com sucesso",3]
    elif voto >= 5:
        return ["Voto nulo computado com sucesso",4]
    else:
        return "Valor inválido"
    # pygame.mixer.music.play()


def estatisticas_de_voto(jose, joao, antonio, votonulo, votobranco):     #Função para exibição de todas estaticas da votação para o usuário final
    totalvotos=(lista_votos[0]+lista_votos[1]+lista_votos[2]+lista_votos[3]+lista_votos[4])
    pernulo = 100*(lista_votos[3]/totalvotos)
    perbranco = 100*(lista_votos[4]/totalvotos)
    print(f"""
    _____________________________________________________________________________________
    |                       NOMES                            |          VOTOS            |
    |________________________________________________________|___________________________|
    |O numero de votos do candidato José                     | {lista_votos[0]}          
    |O numero de votos do candidato João                     | {lista_votos[1]}          
    |O numero de votos do candidato Antônio                  | {lista_votos[2]}          
    |O total de votos nulos é                                | {lista_votos[3]}         
    |O total de votos em branco é                            | {lista_votos[4]}          
    |A percentagem de votos nulos sobre o total de votos é   | {pernulo:.2f}%   
    |A percentagem de votos em branco sobre o total de votos | {perbranco:.2f}%
    |O total de votos é                                      | {totalvotos}
    |________________________________________________________|____________________________|

    """)
 
while True:
    now=datetime.datetime.now()
    ano_atual = now.year
    ano_nascimento=int(input("Informe seu ano de nascimento: "))
    idade_Pessoa=ano_atual-ano_nascimento
    print("Computando voto\n.\n.\n.")
    sleep[1]
    if autoriza_voto_func(idade_Pessoa)=='Voto Opcional' or autoriza_voto_func(idade_Pessoa)=='Voto Obrigatório':
        print(f"""
            CÓDIGO DO CANDIDATO   - NOME DO CANDIDATO   

                                1 - JOSÉ
                                2 - JOÃO
                                3 - ANTÔNIO
                                4 - BRANCO
                                5 - NULO
            """)
        voto = int(input("Digite o código do seu voto: "))
        voto=votacao_Func(voto)
        lista_votos[voto[1]]+=1
        
        print(voto[0])  
    else:
        print(" Você não está autorizado a votar")
    continuar_votando = input("Gostaria de encerrar a votação? [S/N]: ").upper().strip()[0]
    if continuar_votando == 'S':
        break        
estatisticas_de_voto(lista_votos[0],lista_votos[1], lista_votos[2], lista_votos[3], lista_votos[4])

  

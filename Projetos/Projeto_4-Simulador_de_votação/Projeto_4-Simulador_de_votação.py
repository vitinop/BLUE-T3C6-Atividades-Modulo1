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
from time import sleep          # Biblioteca para adicionar deley as ações. 
import pygame                   # Biblioteca para adicionar som.
import datetime                 # Biblioteca para importar a data do computador
total_votos = 0


def autoriza_voto_func(idade_Pessoa,autoriza_voto=''):
        if idade_Pessoa<16:
            autoriza_voto="NEGADO"
            return f'Voto Negado - Você não possui idade suficiente para votar'
        elif idade_Pessoa>=70:
            return f'Voto Opcional'
        else:
            autoriza_voto="OBRIGATÓRIA"
            return f'Voto Obrigatório'


while True:
    now=datetime.datetime.now()
    ano_atual = now.year
    ano_nascimento=int(input("Informe seu ano de nascimento: "))
    idade_Pessoa=ano_atual-ano_nascimento
    print(f"""
            CÓDIGO DO CANDIDATO   - NOME DO CANDIDATO   

                                1 - JOSÉ
                                2 - JOÃO
                                3 - ANTÔNIO
                                4 - BRANCO
                                5 - NULO
            """)            
    votacao_init = input("Gostaria de encerrar a votação? [S/N]: ").upper().strip()[0]
        if votacao == 'S':
            break
        
        
pernulo = 100*(votonulo/totaldevotos)
perbranco = 100*(votobranco/totaldevotos)
print(f"""O numero de votos do candidato José           : {jose}
O numero de votos do candidato João                     : {joao}
O numero de votos do candidato Antônio                  : {antonio}
O numero de votos do candidato Carlos                   : {carlos}
O total de votos nulos é                                : {votonulo}
O total de votos em branco é                            : {votobranco}
A percentagem de votos nulos sobre o total de votos é   : {pernulo:.2f} %
A percentagem de votos em branco sobre o total de votos : {perbranco:.2f}%
""")
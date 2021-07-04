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

class Votacao:  
        def __init__(self,ano_nascimento=0,idade_Pessoa=0):
            import datetime
            now=datetime.datetime.now()
            ano_atual = now.year
            self.ano_nascimento=input("Informe seu ano de nascimento")
            self.idade_Pessoa=ano_atual-self.ano_nascimento
        
        def autoriza_voto_func(self,autoriza_voto=''):
            if self.idade_Pessoa<16:
                self.autoriza_voto="NEGADO"
            elif self.idade_Pessoa>=70:
                self.autoriza_voto="OPCIONAL"
            else:
                self.autoriza_voto="OBRIGATÓRIA"

        def votação_func(self,voto=0):
            if self.autoriza_voto="NEGADO":
                return f"Você não pode votar"
            else:
                self.total_votos +=1

                if voto == 1:
                jose = jose + 1
                return f"Voto no canditadato José computado com sucesso"
                
                elif voto == 2:
                joao = joao +1
                return f"Voto no canditadato João computado com sucesso"
                
                elif voto == 3:
                antonio = antonio+1
                return f"Voto no canditadato Antônio computado com sucesso"
                
                elif voto == 4:
                votobranco += 1
                print("Voto em branco computado com sucesso")
                
                elif voto >= 5 or voto<1:
                votonulo += 1
                print("Voto nulo computado com sucesso")
                
            

        print(f"""
        CÓDIGO DO CANDIDATO   - NOME DO CANDIDATO   

                            1 - JOSÉ
                            2 - JOÃO
                            3 - ANTÔNIO
                            4 - BRANCO
                            5 - NULO
        """)

while True:        
    
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
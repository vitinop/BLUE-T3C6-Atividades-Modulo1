#02 - Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
# O programa vai ler o nome do jogador e quantas partidas ele jogou. 
# Depois vai ler a quantidade de gols feitos em cada partida. 
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

# Vamos aprimorar o código cadastro de jogador de futebol py que foi desenvolvido no Code Lab da aula 14 Faça com que o seu código
# funcione para vários jogadores incluindo um sistema de visualização de detalhes de aproveitamento de cada jogador
class Jogador:
    def __init__(self):
        self.nome = input('Digite o nome do jogador: ')
        self.partidas = int(input('Digite a quantidade de partidas jogadas: '))
        self.golsTotal = int(input('Digite a quantidade de gols: '))
        self.golsPartida = self.golsTotal / self.partidas
    def aproveitamento_func(self):
        return f'''
        Nome: {self.nome}
        Partidas: {self.partidas}
        Gols no Campeonato: {self.golsTotal}
        Aproveitamento: {self.golsPartida:.2f} por partida'''

time = dict()

while True:
    jogador = Jogador()
    time[jogador.nome] = jogador
    print(jogador.aproveitamento_func())
    continuar = input('Quer continuar cadastrando? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break
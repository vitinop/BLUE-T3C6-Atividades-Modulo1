#05 (DESAFIO) Em uma eleição presidencial existem quatro candidatos. 
# Os votos são informados por meio de código.
# Os códigos utilizados são:
# 1 , 2, 3 - Votos para os respectivos candidatos
# (você deve montar a tabela ex: 1 - José / 2- João / etc)
# 5 - Voto Nulo
# 6 - Voto em Branco
# Faça um programa que calcule e mostre:
# O total de votos para cada candidato;
# O total de votos nulos;
# O total de votos em branco;
# A percentagem de votos nulos sobre o total de votos;
# A percentagem de votos em branco sobre o total de votos.
jose = joao = antonio = carlos = totaldevotos = votobranco = votonulo =pernulo = perbranco =0
while True:
    print(f"""
    CÓDIGO DO CANDIDATO   - NOME DO CANDIDATO   

                        1 - JOSÉ
                        2 - JOÃO
                        3 - ANTÔNIO
                        4 - CARLOS
                        5 - VOTO NULO
                        6 - VOTO EM BRANCO 
    """)
    voto = int(input("Digite o código do seu voto: "))
    totaldevotos = totaldevotos+ 1
    if voto == 1:
        jose = jose + 1
        print("Voto no canditadato José computado com sucesso")
    elif voto == 2:
        joao = joao +1
        print("Voto no canditadato João computado com sucesso")
    elif voto == 3:
        antonio = antonio+1
        print("Voto no canditadato Antônio computado com sucesso")
    elif voto == 4:
        carlos = carlos+ 1
        print("Voto no canditadato carlos computado com sucesso")
    elif voto == 5 or voto>6 or voto<1:
        votonulo += 1
        print("Voto nulo computado com sucesso")
    elif voto == 6:
        votobranco += 1
        print("Voto em branco computado com sucesso")
    votacao = input("Gostaria de encerrar a votação? [S/N]: ").upper().strip()[0]
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
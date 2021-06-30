#01 - Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
peso=0
pesomaior=0
pesomenor=10000

for contador in range(0,5) :
    peso=float(input(f"Olá, insira o  peso em kilogramas da {contador+1}ª pessoa :"))
    if (peso>pesomaior):
        pesomaior=peso
    if (peso<pesomenor):
        pesomenor=peso

print (f"""O maior peso inserido foi de {pesomaior}KG
O menor peso inserido foi de {pesomenor}KG""")
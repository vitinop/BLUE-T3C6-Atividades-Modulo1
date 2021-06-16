#03 - Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
idade=0
contadormaior=0
contadormenor=0

for contadoridade in range(0,7) :
    idade=int(input(f"Olá, insira a idade da {contadoridade+1}ª pessoa :"))
    if (idade>=18):
        contadormaior=contadormaior+1
    else:
        contadormenor=contadormenor+1

print (f"""O número de pessoas que já atingiram a maioridade é : {contadormaior}
O número de pessoas que ainda não atingiram a maioridade é : {contadormenor}""")

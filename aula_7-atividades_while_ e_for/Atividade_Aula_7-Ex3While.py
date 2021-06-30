#03 - Crie um programa que leia o nome e o preço de vários produtos.
#  O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#(A) Qual é o total gasto na compra.
#(B) Quantos produtos custam mais de R$1000.
#(C) Qual é o nome do produto mais barato.
total=0
contadormaiscaro=0
valormaisbarato=10000000
nomemaisbarato=" "
controle=" "
while controle!="S":
    nome=str(input("Olá, insira o nome do produto : "))
    valor=float(input("Olá, informe o valor do produto: "))
    total=total+valor
    if valor>1000: 
        contadormaiscaro=contadormaiscaro+1
    elif valormaisbarato>valor:
        nomemaisbarato=nome
    print(f"""
    O valor total da compra é: R${total}
    O número de produtos que custam mais que R$1000 é : {contadormaiscaro}
    O nome do produto mais barato é: {nomemaisbarato}""")

    controle=("Gostaria de encerrar o programa ? [S/N]")
    controle=controle.upper().strip()[0]
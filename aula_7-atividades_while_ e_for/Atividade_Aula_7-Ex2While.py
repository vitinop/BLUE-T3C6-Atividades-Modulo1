#02 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada
#pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não
#continuar. No final, mostre:
#A) Quantas pessoas têm mais de 18 anos.
#B) Quantos homens foram cadastrados.
#C) Quantas mulheres têm menos de 20 anos.
controle=" "
contadormidade=0
contadormulher=0
contadorhomem=0

while controle!="S":
    idade=int(input("Olá, insira a idade da pessoa :"))
    sex=str(input("Olá, informe o sexo biologico da pessoa, digite F para feminino e M para masculino: "))
    sex=sex.upper()
    if idade>=18:
        contadormidade=contadormidade+1
        if sex=="M":
            contadorhomem=contadorhomem+1
        elif idade<20 and sex=="F":
            contadormulher=contadormulher+1
            
    
                   
    print(f"""
    O número de pessoas com mais de 18 é: {contadormidade}
    O número de homens cadastrados é: {contadorhomem}
    O número de mulheres com menos de 20 anos é: {contadormulher}""")
    controle=("Gostaria de encerrar o programa ? [S/N]")
    controle=controle.upper().strip()[0]

#04 - Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
# Se o valor digitado for ímpar, desconsidere-o.
# Mostre também quantos valores pares foram digitados.
contadorpar=0
soma=0
for contadordenumeros in range(0,6) :
    num=int(input(f"Olá, insira um número inteiro:"))
    if (num % 2 ==0):
        contadorpar=contadorpar+1
        soma=soma+num
    
        

print (f"""A soma dos numeros pares inseridos é: {soma}
O numero total de números pares inseridos é: {contadorpar}""")
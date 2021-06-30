#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso. (utilizar while sem break)
from time import sleep
usernumber =float (input ("Insira um o primeiro valor: "))
usernumber2 =float (input ("Insira um o segundo valor: "))

while controle != 5:
    controle=int((input ("""
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa  
    
    Selecione uma Opção e pressione enter: """)))
    if controle==1:
        print(f"A soma dos numeros é : {usernumber+usernumber2}")
    elif controle==2:
         print(f"A multiplicação dos numeros é : {usernumber*usernumber2}")
    elif controle==3:
        if usernumber>usernumber2:
            print(f"O numero maior é: {usernumber}")
        elif usernumber2>usernumber:
            print(f"O numero maior é: {usernumber2}")
        elif usernumber2==usernumber:
            print(f"O numero {usernumber} e {usernumber2} tem o mesmo valor")
    elif controle==4:
        usernumber =float (input ("Insira um o primeiro valor: "))
        usernumber2 =float (input ("Insira um o segundo valor: "))
    elif controle>5 or controle<1:
        print("Comando inválido, Informe novamente a ação desejada")
print("Você finalizou o programa com sucesso !")


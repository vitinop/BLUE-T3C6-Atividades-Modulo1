# #02 - Crie um programa que vai ler vários números e colocar em uma lista. Depois
# disso, crie duas listas extras que vão conter apenas os valores pares e os valores
# ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas
# geradas.
lista=[]
listaPar=[]
listaImpar=[]
numero=0
while True:
    numero= int(input("Insira um numero inteiro na lista: "))
    lista.append(numero)
    if numero%2==0:
        listaPar.append(numero)
    else:
        listaImpar.append(numero)
    encerrar = input("Gostaria de encerrar o programa e exibir a lista de valores unicos digitados? [S/N]: ").upper().strip()[0]
    if encerrar == 'S':
        break
print(f"""
A lista total contem: {lista}
A lista de numeros pares inseridos na lista total é:{listaPar}
A lista de numeros impares inseridos na lista total é:{listaImpar}
""")
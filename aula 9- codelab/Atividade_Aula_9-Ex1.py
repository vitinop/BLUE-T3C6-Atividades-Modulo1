# #01 - Crie um programa onde o usuário possa digitar vários valores numéricos e
# cadastre-os em uma lista. Caso o número já esteja lá dentro, ele não será
# adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem
# crescente.
lista=[]
numero=0
while True:
    numero= int(input("Insira um numero inteiro na lista: "))
    if numero not in lista:
        lista.append(numero)

    encerrar = input("Gostaria de encerrar o programa e exibir a lista de valores unicos digitados? [S/N]: ").upper().strip()[0]
    if encerrar == 'S':
        break
print(f"A lista de números unicos inseridos pelo usuário é: {sorted(lista)}")
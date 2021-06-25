# Faça um programa, com uma função que necessite de um parametro. 
# A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
def verificar_positivo():
    num=int(input("Insira um numero  para descobrir se ele é positivo ou negativo: "))
    if num > 0:
        return f'P' 
    elif num <= 0:
        return f'N'
    
   
numero=verificar_positivo()
print(numero)
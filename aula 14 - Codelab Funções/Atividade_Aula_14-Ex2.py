# 2. Faça um programa, com uma função que necessite de um argumento. 
# A função retorna o valor de caractere ‘P’, se seu argumento for positivo, ‘N’, se seu argumento for negativo e ‘0’ se for 0.
def verificar_positivo():
    num=int(input("Insira um numero  para descobrir se ele é positivo ou negativo: "))
    if num > 0:
        return f'P' 
    elif num < 0:
        return f'N'
    else:
        return f'0'
    
numero=verificar_positivo()
print(numero)
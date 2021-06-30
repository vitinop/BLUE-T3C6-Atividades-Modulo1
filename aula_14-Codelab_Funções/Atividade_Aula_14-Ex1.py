# 1. Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
def soma(n1=0,n2=0,n3=0):
    soma_resultado=0
    for i in range (1,4):
        n=int(input(f"Digite o {i}º valor: "))
        soma_resultado=soma_resultado+n
    return(soma_resultado)
resultado=soma()
print(f"O Resultado da soma é : {resultado}")

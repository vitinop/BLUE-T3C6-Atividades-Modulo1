# 7. Escreva uma função que recebe dois parâmetros e imprime o menor dos dois. 
# Se eles forem iguais, imprima que eles são iguais.
def maiornumero(num1=0,num2=0):
    num1=(input("Insira o primeiro numero: "))
    num2=(input("Insira o segundo numero: "))
    if num1>num2:
        return f"O primeiro número inserido é o maior, tendo valor de : {num1}"
    elif num2>num1:
        return f"O segundo número inserido é o maior, tendo valor de : {num2}"
    elif num1==num2:
        return f"Os números inseidor são iguais, tendo valor: {num2} "
maior=maiornumero()
print(maior)